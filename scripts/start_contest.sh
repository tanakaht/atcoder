#!/bin/bash

contest_name=$1
if [ $2 ]; then
  type=$2
else
  type="py"
fi
problems="a,b,c,d,e,f,g,h"
contest_dir=./contests/${contest_name}_${type}

# dir作成
mkdir "./contests/${contest_name}_${type}"
mkdir ${contest_dir}/src
mkdir ${contest_dir}/.vscode
mkdir ${contest_dir}/testcases
touch ${contest_dir}/testcases/input.txt
# reviewファイル用意
sed "s/<CONTESTNAME>/${contest_name}/g" templates/review.md > ${contest_dir}/${contest_name}_review.md

# pyの時
if [ "$type" = "py" ]; then
  templatedir=templates/template_py
  # srcファイル作成
  for problem in ${problems//,/ }; do
    cp ${templatedir}/src/sample.py ${contest_dir}/src/${contest_name}_${problem}.py
  done
  cp ${templatedir}/src/experiment.ipynb ${contest_dir}/src/experiment.ipynb
  # scriptコピー
  cp -r ${templatedir}/scripts ${contest_dir}/scripts
  # .vscodeの作成
  sed "s/<CONTESTNAME>/${contest_name}/g" ${templatedir}/.vscode/launch.json > ${contest_dir}/.vscode/launch.json
  sed "s/<CONTESTNAME>/${contest_name}/g" ${templatedir}/.vscode/tasks.json > ${contest_dir}/.vscode/tasks.json
  sed "s/<CONTESTNAME>/${contest_name}/g" ${templatedir}/.vscode/settings.json > ${contest_dir}/.vscode/settings.json

# rustの時
elif [ "$type" = "rust" ]; then
  templatedir=templates/template_rust
  # srcファイル作成
  for problem in ${problems//,/ }; do
    cp ${templatedir}/src/sample.rs ${contest_dir}/src/${contest_name}_${problem}.rs
  done
  # scriptコピー
  cp -r ${templatedir}/scripts ${contest_dir}/scripts
  # Cargo.toml, Cargo.lock
  sed "s/<CONTESTNAME>/${contest_name}/g" ${templatedir}/Cargo_a2h.toml > ${contest_dir}/Cargo.toml
  sed "s/<CONTESTNAME>/${contest_name}/g" ${templatedir}/Cargo.lock > ${contest_dir}/Cargo.lock
  # .vscodeの設定ファイル
  sed "s/<CONTESTNAME>/${contest_name}/g" ${templatedir}/.vscode/launch.json > ${contest_dir}/.vscode/launch.json
  sed "s/<CONTESTNAME>/${contest_name}/g" ${templatedir}/.vscode/tasks.json > ${contest_dir}/.vscode/tasks.json
  sed "s/<CONTESTNAME>/${contest_name}/g" ${templatedir}/.vscode/settings.json > ${contest_dir}/.vscode/settings.json

# マラソンの時
elif [ "$type" = "marathon" ]; then
  exit 0
fi

# vscodeで開く
code ${contest_dir}
