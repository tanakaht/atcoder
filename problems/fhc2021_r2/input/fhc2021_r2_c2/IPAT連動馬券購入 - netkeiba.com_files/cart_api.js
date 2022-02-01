/*
 * $Id: cart_api.js 293 2017-08-16 09:19:22Z ysimizu $
 *
 *  汎用カートAPI(ver2.0)
 *    require 'jquery.js';
 *  
 *  2017.8.15 Y.Shimizu
 *
 */
var NDCartApi = (function(){
    var _debug;
    var _action_api_url;
    var _type;
    
    // constructor
    var NDCartApi = function( url_api, type, debug ){
        self = this;

        _debug = (undefined === debug) ? false : debug;
        if(_debug) console.log('NDCartApi(%s,%s,%s)', url_api, type, debug);

        if(undefined === url_api){
	        console.error("empty parameter 'url_api'");
	        return false;
        }
        _url_api = url_api;
        if(undefined === type){
            _type = 'jsonp';
        }else{
            _type = type;
        }
    }

    var proto = NDCartApi.prototype;

    /*
     * カート内容を取得する
     */
    proto.get_item_list = function( group, fn )
    {
        var self = this;
        if(_debug)	console.log('get_item_list(%s)',group);

        var param = {
	        action: 'get',
	        group: group, 
        };
        self.http_request(_url_api, param, function( resp ){
	        if(undefined !== resp.status && 'NG' == resp.status){
	            console.error('status=NG');
	        }
	        if(undefined !== fn){
	            fn(resp);
	        }
        });
    }

    /*
     * カートのアイテム数を取得する
     */
    proto.get_item_count = function( group, fn )
    {
        var self = this;
        if(_debug)	console.log('get_item_count(%s)',group);

        var param = {
	        action: 'count',
	        input: 'UTF-8',
	        output: _type,
	        group: group, 
        };
        self.http_request(_url_api, param, function( resp ){
	        if(undefined !== resp.status && 'NG' == resp.status){
	            console.error('status=NG');
	        }
	        if(undefined !== fn){
	            fn(resp);
	        }
        });
    }

    /*
     * カートにアイテムを追加・更新する
     */
    proto.add_item = function( group, item_id, item_value, item_price, client_data, fn )
    {
        var self = this;
        if(_debug) console.log('add_item(%s,%O,%O,%O,%O)',group,item_id,item_value,item_price,client_data);

        var param = {
	        action: 'add',
	        group: group, 
	        item_id: item_id, 
	        item_value: item_value,
	        item_price: item_price, 
	        client_data: client_data,
        };
        self.http_request(_url_api, param, function( resp ){
	        if(undefined !== resp.status && 'NG' == resp.status){
	            console.error('status=NG');
	        }
	        if(undefined !== fn){
	            fn(resp);
	        }
        });
    }

    /*
     * カートにアイテムを追加する
     * (グループIDドメインのデータを削除後に追加したアイテムで置き換える)
     */
    proto.replace_item = function( group, item_id, item_value, item_price, client_data, fn )
    {
        if(_debug) console.log('replace_item(%s,%O,%O,%O,%O)',group,item_id,item_value,item_price,client_data);

        var param = {
	        action: 'replace',
	        group: group, 
	        item_id: item_id, 
	        item_value: item_value,
	        item_price: item_price, 
	        client_data: client_data,
        };
        self.http_request(_url_api, param, function( resp ){
	        if(undefined !== resp.status && 'NG' == resp.status){
	            console.error('status=NG');
	        }
	        if(undefined !== fn){
	            fn(resp);
	        }
        });
    }

    /*
     * カートからアイテムを削除する
     */
    proto.remove_item = function( group, item_id, fn )
    {
        var self = this;
        if(_debug) console.log('remove_item(%s,%s)',group,item_id);

        var param = {
	        action: 'remove',
	        group: group, 
	        item_id: item_id, 
        };
        self.http_request(_url_api, param, function( resp ){
	        if(undefined !== resp.status && 'NG' == resp.status){
	            console.error('status=NG');
	        }
	        if(undefined !== fn){
	            fn(resp);
	        }
        });
    }

    /*
     * カートをクリアする
     */
    proto.clear_item = function( group, fn )
    {
        var self = this;
        if(_debug) console.log('clear_item(%s)',group);

        var action = null !== group ? 'clear' : 'clear_all';
        var param = {
	        action: action,
        };
        if(null !== group){
	        param['group'] = group; 
        }

        self.http_request(_url_api, param, function( resp ){
	        if(undefined !== resp.status && 'NG' == resp.status){
	            console.error('status=NG');
	        }
	        if(undefined !== fn){
	            fn(resp);
	        }
        });
    }

    /*
     *  private
     *  HTTP Request
     */
    proto.http_request = function( api_url, param, fn )
    {
        var self = this;
        if(_debug) console.log('http_request(%s,%O)',api_url,param);

        var default_param = {
	        input:  'UTF-8',
	        output: _type,
        };
        var add_param = default_param;
        for(var key in param){
	        add_param[key] = param[key];
        }
        if(_debug) console.log('add_param: ',add_param);

        var http_type = 'get';
        if('json' == _type){
            http_type = 'post';
        }
        $.ajax({
            type: http_type,
            url:  _url_api,
            data: add_param,
            dataType: _type,
            xhrFields: {
                withCredentials: true
            },
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

    return NDCartApi;
})();
