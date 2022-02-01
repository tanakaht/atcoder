
/*
 * $Id: nd_isam.js 1652 2018-02-16 12:08:44Z ysimizu $
 *
 *  ブラウザ用ローカルストレージ利用、汎用ISAM
 * 
 *  2017.8.10 Y.Shimizu
 *  require
 *     store.js
 */

var NDIsam = function( debug )
{
    var self = this;
    self.debug = (undefined === debug) ? false : debug;
    if(self.debug) console.log('NDIsam(%s)', debug);

    self.lskey_prefix = 'ndi::';
};

/*
 * データ一覧を取得
 */
NDIsam.prototype.list = function( domain )
{
    var self = this;
    if(self.debug) console.log('NDIsam.list(%s)',domain);

    var lskey = self.lskey_prefix + domain;
    var rbuf = store.get(lskey);
    if(! rbuf){
	console.error('empty data !! domain: %s',domain);
	return false;
    }else{
	return rbuf['list'];
    }
}

/*
 * アイテムを追加・置換(単一レコード)
 */
NDIsam.prototype.replace = function( domain, rec_key, rec_value )
{
    var self = this;
    if(self.debug) console.log('NDIsam.add(%s,%s,%s)',domain,rec_key,rec_value);
    
    // initial format
    var store_def = {
	list: {},	// key,value array
	uptime: null,
    };

    var dt = new Date();
    var lskey = self.lskey_prefix + domain;
    var wbuf = null;
    var rbuf = store.get(lskey);
    if(! rbuf){
	wbuf = store_def;
    }else{
	wbuf = rbuf;
    }

    wbuf['list'][rec_key] = rec_value;
    wbuf['uptime'] = self._format_date(dt,'YYYY-MM-DD hh:mm:ss');
    var ret = store.set(lskey, wbuf);
    return ret ? true : false;
}

/*
 * アイテム削除(単一レコード)
 */
NDIsam.prototype.remove = function( domain, rec_key )
{
    var self = this;
    if(self.debug) console.log('NDIsam.add(%s,%s)',domain,rec_key);
    
    var dt = new Date();
    var lskey = self.lskey_prefix + domain;

    var rbuf = store.get(lskey);
    if(! rbuf){
	console.error('empty data !! domain: %s',domain);
	return false;
    }
    var wbuf = rbuf;
    if(! wbuf['list'][rec_key]){
	console.error('not found !! key: %O',rec_key);
	return false;
    }
    delete wbuf['list'][rec_key];
    wbuf['uptime'] = self._format_date(dt,'YYYY-MM-DD hh:mm:ss');
    var ret = store.set(lskey, wbuf);
    return ret ? true : false;
}

/*
 * アイテム削除(ALL)
 */
NDIsam.prototype.clear = function( domain )
{
    var self = this;
    if(self.debug) console.log('NDIsam.clear(%s)',domain);
    
    var lskey = self.lskey_prefix + domain;
    store.remove(lskey);
    return true;
}

/*
 * private
 * 日付をフォーマットする
 */
NDIsam.prototype._format_date = function(date, format) {
    if (!format) format = 'YYYY-MM-DD hh:mm:ss.SSS';
    format = format.replace(/YYYY/g, date.getFullYear());
    format = format.replace(/MM/g, ('0' + (date.getMonth() + 1)).slice(-2));
    format = format.replace(/DD/g, ('0' + date.getDate()).slice(-2));
    format = format.replace(/hh/g, ('0' + date.getHours()).slice(-2));
    format = format.replace(/mm/g, ('0' + date.getMinutes()).slice(-2));
    format = format.replace(/ss/g, ('0' + date.getSeconds()).slice(-2));
    if (format.match(/S/g)) {
	var milliSeconds = ('00' + date.getMilliseconds()).slice(-3);
	var length = format.match(/S/g).length;
	for (var i = 0; i < length; i++)
	    format = format.replace(/S/, milliSeconds.substring(i, i + 1));
    }
    return format;
};



