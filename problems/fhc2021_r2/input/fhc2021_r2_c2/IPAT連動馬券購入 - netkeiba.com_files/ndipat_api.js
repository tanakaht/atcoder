
"use strict" 
/*
 * $Id: ndipat_api.js 2019 2018-06-15 07:24:10Z ysimizu $
 *
 *  JRA,海外,NAR IPATサイト連携 API
 *
 *  2018.6.12 Y.Shimizu 新規
 *  require  jquery.js
 */

var NDIpatApi = (function(){
    var _debug;
    var _action_api_url;
    var _syusai;
    
    // constructor
    var NDIpatApi = function( action_api_url, syusai, debug ) {
        var self = this;

        _debug = (undefined === debug) ? false : debug;
        if(_debug) console.log('NDIpatApi(%s,%s,%s)',action_api_url,syusai,debug);

        if(undefined === action_api_url){
	        return false;
        }
        _action_api_url = action_api_url;
        _syusai = syusai;
    }

    var proto = NDIpatApi.prototype;

    /*
     * IPATサービスがオープン中か？
     */
    proto.check_service = function( fn ){
        var self = this;
        if(_debug) console.log('check_service()');
        
        if(undefined === fn){
	        console.error('callback function not defined');
	        return false;
        }

        var param = {
	        action: 'check_service',
	        syusai: _syusai,
	        ipat_number: 'dummy',
	        ipat_passwd: 'dummy',
	        ipat_pars: 'dummy',
        };
        self.http_request(_action_api_url, 'jsonp', param, function( resp ){
	        if(undefined !== resp.status && 'NG' == resp.status){
		        fn( false );
	        }
            fn( resp );
        });
    }

    /*
     * 保存したログイン情報を取得
     */
    proto.get_login_info = function( fn ){
        var self = this;
        if(_debug) console.log('get_login_info()');
        
        if(undefined === fn){
	        console.error('callback function not defined');
	        return false;
        }

        var param = {
	        action: 'get_info',
	        syusai: _syusai,
        };
        self.http_request(_action_api_url, 'jsonp', param, function( resp ){
	        if(undefined !== resp.status && 'NG' == resp.status){
		        fn( false );
	        }
            fn( resp );
        });
    }

    /*
     * IPAT連携サイトにログインする
     */
    proto.login = function( number, passwd, pars, is_save, fn ){
        var self = this;
        if(_debug) console.log('login(%s,%s,%s,%s)',number,passwd,pars,is_save);
        
        if(undefined === fn){
	        console.error('callback function not defined');
	        return false;
        }

        var param = {
	        action: 'login',
	        syusai: _syusai,
	        ipat_number: number,
	        ipat_passwd: passwd,
	        ipat_pars: pars,
	        is_save: is_save,
        };
        self.http_request(_action_api_url, 'jsonp', param, function( resp ){
	        if(undefined !== resp.status && 'NG' == resp.status){
		        fn( false );
	        }
            fn( resp );
        });
    }

    /*
     * IPAT連携サイトに投票する
     */
    proto.bet = function( number, passwd, pars, ary_kaime, fn ){
        var self = this;
        if(_debug) console.log('bet(%s,%s,%s,%O)',number,passwd,pars,ary_kaime);
        
        if(undefined === fn){
	        console.error('callback function not defined');
	        return false;
        }

        var param = {
	        action: 'bet',
	        syusai: _syusai,
	        ipat_number: number,
	        ipat_passwd: passwd,
	        ipat_pars: pars,
	        ary_kaime: ary_kaime,
        };
        self.http_request(_action_api_url, 'jsonp', param, function( resp ){
	        if(undefined !== resp.status && 'NG' == resp.status){
		        fn( false );
	        }
            fn( resp );
        });
    }

    /*
     *  private
     *  HTTP Request type: 'json' or 'jsonp'
     */
    proto.http_request = function( api_url, type, param, fn ){
        var self = this;
        if(_debug) console.log('http_request(%s,%O)',api_url,param);
        var default_param = {
	        input:  'UTF-8',
	        output: ('json' == type) ? 'json' : 'jsonp',
        };
        var add_param = default_param;
        for(var key in param){
	        add_param[key] = param[key];
        }
        if(_debug) console.log('add_param: ',add_param);

        $.ajax({
            type: 'GET',
            url:  _action_api_url,
            data: add_param,
            dataType: type,
            success  : function( data ){
                fn(data);
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                console.error('XMLHttpRequest.status: ',XMLHttpRequest.status)
                console.error('textStatus: ',textStatus);
                console.error('errorThrown.message: ',errorThrown.message);
            }
        });
    }
    return NDIpatApi;
})();

