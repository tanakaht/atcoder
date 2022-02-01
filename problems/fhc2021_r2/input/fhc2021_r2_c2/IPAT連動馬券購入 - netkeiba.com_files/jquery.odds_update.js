/**
 * ���å�����
 *
 * options
 * @param apiUrl            api domein������
 * @param raceId            race_id ������
 * @param isPremium         1:ͭ����� 0:̵�����
 * @param oddsType          1 :(ñ��ʣ���ϥ��å�) 3:��Ϣ 4:��Ϣ 5:�磻�� 6:��ñ 7:��Ϣʣ 8:��Ϣñ all:������
 * @param sort              odds:����(no) ninki:�͵���
 *                              odds : view�ؿ��Ѱդ��Ƥ���ޤ�����ɬ�פ˱����ơ�callbackApiOverrideView���ȼ��������Ƥ�������
 *                              ninki��ξ�硢view��ʬ���Ѱդ��Ƥ��ʤ��Τǡ�callbackApiOverrideView�����ȼ��������Ƥ�������
 *
 * @param autoUpdate        true:������ǽͭ�� false:������ǽ̵��
 * @param cookieName        auto_odds ��ư����Ƚ����cookei̾
 * @param intervalTimer     ��ư���������ޡ�
 * @param isBrackets        true : (*�͵�) false: *�͵� �͵���()��Ĥ��뤫
 * @param isDiffValueAnim   true : ���å���Ӹ奢�˥᡼�����class�����ꤹ�� false : ���ꤷ�ʤ�
 * @param displayDiffTime   true : ���л���ͭ�� false : ���л���̵��
 * @param update_limit      ̵��������ι������(js��php�������꤬ɬ��) Todo:�ѥ�᡼�����Ϥ���褦�ˤ���
 *
 * @param compressa     true : ����ͭ�� false : ����̵�� �ǡ����̤�¿������� true�侩
 * @param debugMode     true:console.logɽ�� false:console.log��ɽ��
 *
 */
(function( $ ) {

    var s = {}; //����
    var data = {}      //�ǿ����å�
    var horse_list = {};//ninki����̾
    var odds_status = ''; //�������å����ơ�����
    var user_update_count = 0;//̵���桼�����ι������
    var connecting_flg;//Ϣ���ɻ�

    var diff_odds = {};//�������å������
    var diff_first_flg = true;//���å���ӽ��Ƚ��ե饰
    var mdomain = document.domain.substr( document.domain.lastIndexOf(".netkeiba") );
    var domain = mdomain; //cookie�ѥɥᥤ��
    var obj_interval = null;
    //default ����
    var defaults = {
        apiUrl        : '', //ɬ��
        raceId        : '', //ɬ��
        isPremium     : '', //ɬ��
        oddsType      : 1,
        sort          : 'odds',
        autoUpdate    : true,
        intervalTimer : 30000, //30sec
        isBrackets    : true,
        isDiffValueAnim : true,
        displayDiffTime : true,
        update_limit  : 5,
        compress      : true,
        debugMode     : false,

        PremiumLinkReturnUrl : '', //ͭ�������Ͽ�������
        PremiumLinkReturnRf  : 'odds',//����¬���ѥ�ե���

        //cookie
        cookieName          : 'auto_odds', //��ư����on or off

        //event selector
        oddsAutoUpdate   : 'act-auto_update'    , //��ư�������٥��
        oddsManualUpdate : 'act-manual_update', //��ư�������٥��

        //selector
        oddsUpdatePrefixId        : 'odds-',       //���å�ɽ��prefix {oddsUpdatePrefixId}-{type}_{umaban} ���Ѵ�
        ninkiUpdatePrefixId       : 'ninki-',      //���å�ɽ��(�͵���)prefix {ninkiUpdatePrefixId}-{rank|no|name}_{umaban} ���Ѵ�
        oddsUpdateColorClass      : 'transition-color', //���å���Ӹ�Υե���ȥ��顼(���˥᡼�����)
        oddsUpdateBackgroundclass : 'Popular',     //���å���ӥ���class
        oddsUpdateBackgroundColor : 'UpdateOdds',  //���å���Ӹ���ɲå���class(���˥᡼�����)
        updateOfficialTimeId      : 'official_time',   //��������ʸ��
        liveOddsUpdate            : 'LiveOddsUpdate',   //��֥��å����˥��å������ܥ��󡢼�ư�����ܥ����ɽ��
        updateCount               : 'OddsUpLimitCount',    //�������

        //modal selector
        popupShowId    : 'free_odds_limit_overlay', //popup��������
        popupContentId : 'inline_content',       //popup ����

        //callbacks
        callbackLoad    : false,
        callbackApiLoad : false,
        callbackApiOverrideView : false, //���̤ˤ�ä�view��ʬ���ȼ�������ɬ�פʾ��
        callbackApiComplete: false,
        callbackComplete   : false
    };

    //main
    $.oddsUpdate = function( options ) {

        var isCompress = _checkCompress();
        //����
        s = $.extend({}, defaults, options );
        var isCompress = _checkCompress();
        if(!isCompress) {
            s.compress = false;
        }
        var setting = s;

        //load calllback
        if(s.callbackLoad) {
            s.callbackLoad(this);
        }

        if(s.debugMode) console.log('settings : ',s);

        //modal����
        if(s.isPremium == 0) {
            _getOddsModal(s.popupShowId);
        }
        //cookie�ν����
        var ymd = _getDateYmd();
        if(getCookie(s.cookieName)) {
            var auto_odds_val = getCookie(s.cookieName);
            if(ymd != auto_odds_val) {
                document.cookie = sprintf("%s=;max-age=0",s.cookieName);
            }
        }

        //���å�������
        s.action = 'init';
        _updateOdds();

        //�ʲ����٥��
        s.action = 'update';
        
        //ͭ�����
        if(s.autoUpdate) {
            if(getCookie(s.cookieName) && s.isPremium == 1){
                if(s.debugMode) console.log('cookie exists');
                $('#'+s.oddsAutoUpdate).prop("checked",true);
                clearInterval(obj_interval);
                obj_interval = setInterval(function(){_updateOdds(true, true)}, s.intervalTimer);//update
            }else{
                document.cookie = sprintf("%s=;max-age=0",s.cookieName);//�ꥻ�å�
                $('#'+s.oddsAutoUpdate).prop("checked",false);
                if(s.debugMode) console.log('cookie emtpy');
            }
        }

        //��ư����on off
        $(document).off('click', "#"+s.oddsAutoUpdate).on('click', "#"+s.oddsAutoUpdate, function(){
            this.autoUpdateOdds = true;
            if(s.isPremium == 1) {
                if(getCookie(s.cookieName)){
                    if(s.debugMode) console.log('remove cookie');
//                    document.cookie = sprintf("%s=;max-age=0",s.cookieName);
                    document.cookie = s.cookieName + '=' + ymd + '; path=/; max-age=0; domain=' + domain + ';';

                    clearInterval( obj_interval );
                }else{
                    if(s.debugMode) console.log('set cookie');
                    //var ymd = _getDateYmd();
                    //setCookie(s.cookieName, ymd, 1);
                    var now = new Date();
                    now.setDate(now.getDate() + 1)
                    var expires = now.toGMTString();
                    clearInterval( obj_interval );
                    document.cookie = s.cookieName + '=' + ymd + '; path=/; expires=' + expires + '; domain=' + domain + ';';
                    obj_interval = setInterval(function(){_updateOdds(true, true)}, s.intervalTimer);
                }
            } else {
                //popup
                $('#'+s.oddsAutoUpdate).prop("checked",false);
                document.cookie = sprintf("%s=;max-age=0",s.cookieName);
                _popupView(1);
            }
        });

        // //�����ܥ��󲡲�
        $(document).off('click', "#"+s.oddsManualUpdate).on('click', "#"+s.oddsManualUpdate, function(){
            this.autoUpdateOdds = false;
            _updateOdds(true, false);
        });
        
        //modal ͭ��������
        $(document).on('click','.oddPremiumPayment',function(){
            $.colorbox.close(); //colorbox �Ĥ���
            var next_url = $(this).data('next_url');
            if(s.PremiumLinkReturnUrl) {
                next_url += '&return_url='+s.PremiumLinkReturnUrl;
            }
            if(s.PremiumLinkReturnRf) {
                next_url += '&rf='+s.PremiumLinkReturnRf;
            }
            location.href = next_url;
        });

        //complete calllback
        if(s.callbackComplete) {
            s.callbackComplete(this);
        }

        return(this);
    }

    /*****private****
     *
     * format_update_time �Τ�public
     */

    /**
     * ���å�����
     */
    var _updateOdds = function(updateManual, autoUpdateOdds){

        if(s.debugMode) console.log('function _updateOdds');
        if (autoUpdateOdds) {
            this.autoUpdateOdds = true;
        } else {
            this.autoUpdateOdds = false;
        }
        if(s.isDiffValueAnim) {
            var animationNode = $('.'+s.oddsUpdateBackgroundclass);
            animationNode.each(function(){
                $(this).removeClass(s.oddsUpdateBackgroundColor);
                $(this).find('[id^='+s.oddsUpdatePrefixId+']').removeClass(s.oddsUpdateColorClass);
            });
            //�������å������
            $('[id^="'+s.oddsUpdatePrefixId+'"]').each(function(){
                var key = $(this).prop('id');
                var val = $(this).text();
                diff_odds[key] = val;
            });
        }

        if(s.action == 'update') diff_first_flg = false;
        _getOdds(s.raceId, s.oddsType, s.action, s.sort, function(resp){
            //load calllback
            if(s.callbackApiLoad) {
                s.callbackApiLoad(this, odds_status, data);
            }

            if(resp.status=='middle'){
                if(s.debugMode) console.log('show oddsUpdateButton');
                $('.'+s.liveOddsUpdate).show();
                if(s.isPremium == 0) $('.OddsUpLimitTxt02').show();
                // $(".RaceInfo_Notice").attr('class').split(/\s+/);
                $(".RaceInfo_Notice").removeClass('mt18');
                $(".RaceInfo_Notice").addClass('mt10');
            }

            if(s.debugMode) console.log('resp: %O',resp);

            data = resp.data;

            odds_status = resp.status;
            user_update_count = resp.update_count;
            var update_limit = s.update_limit - user_update_count;
            $('#'+s.updateCount).html(update_limit);

            //view���ȼ��˼������������
            if(s.callbackApiOverrideView){
                switch(resp.status) {
                    case 'limit':
                        _popupView(2, s.update_limit );
                        break;
                    case 'NG':
                        console.log(resp.reason);
                        break;
                    default:
                        this.updateManual = updateManual;
                        s.callbackApiOverrideView(this, resp);
                }
            } else {
                switch(resp.status) {
                  case 'result':
                    _updateResultOddsView();
                    break;
                  case 'middle':
                    _updateOddsView(autoUpdateOdds);
                    break;
                  case 'yoso':
                    _updateYosoOddsView();
                    break;
                  case 'limit':
                    _popupView(2, s.update_limit );
                    break;
                  case 'NG':
                      console.log(resp.reason);
                    break;
                }
            }

            //complete calllback
            if(s.callbackApiComplete) {
                s.callbackApiComplete( this, odds_status, data );
            }
        });
    }

    /**
     * ���å�����
     *
     * 2018.04.11 d.ito
     * axsios��ZLIB�ʤ�android4.0�ʲ����б��Ǥ��ʤ��ΤǤ������Ȥ�
     *
     */
    var _getOdds = function(raceId, oddsType, action, sort, _callback){

        var _data = { pid : 'api_get_jra_odds' };
        _data.input   = 'UTF-8';
        _data.output  = 'jsonp';

        _data.race_id = raceId;
        _data.type = oddsType;
        _data.action = action;
        _data.sort = sort;
        _data.compress = s.compress ? 1 : 0;
        $.ajax( { type     : 'GET',
            url      : s.apiUrl,
            data     : _data,
            dataType : _data.output,
            success  : function( resp )
            {
                var data_body;
                if(_data.compress == 1){
                    if(resp.data !== ''){
                        var z_stream = ZLIB.inflateInit();
                        var oj = z_stream.inflate( base64decode(resp.data) );
                        if(oj == ''){
                            console.log('inflate error');
                            return;
                        }
                        data_body = JSON.parse(oj);
                        resp.data = data_body;
                    }
                }
                _callback(resp);
            },
            error  : function(XMLHttpRequest, textStatus, errorThrown)
            {
                console.log('XMLHttpRequest: %O',XMLHttpRequest);
                console.log('textStatus: %s',textStatus);
            }
        });
    }

    /**
     * ͽ�ۥ��å�ɽ��(odds��) ñ���Τ�
     */
    var _updateYosoOddsView = function (){

        if(s.debugMode) console.log('function _updateYosoOddsView');

        // ���å���������
        $('[id='+s.updateOfficialTimeId+']').text( format_update_time(data['official_datetime']) );

        var odds = data['odds'];
        $('[id^="'+s.oddsUpdatePrefixId+'"]').each(function(){
            var diff_key = $(this).prop('id');
            var tmp_data_key = $(this).attr('id').split('-');
            var data_key = tmp_data_key[1].split('_');
            var type = data_key[0];
            var odds_key = data_key[1];
            var row = odds[type][odds_key];
            var key_ninki_rank = sprintf(s.ninkiUpdatePrefixId+'%1s_%s', type, odds_key);

            if (row) {
                $(this).html(row[0]);
            
                if(s.isBrackets) {
                    $('#'+key_ninki_rank).text( '('+row[2]+')' );
                } else {
                    $('#'+key_ninki_rank).text( row[2] );
                }

                if(diff_odds[diff_key] != row[0] && s.isDiffValueAnim){
                    diff_odds[diff_key] = row[0];
                    $('[id='+diff_key+']').addClass(s.oddsUpdateColorClass);
                }
            }
        });
    }


    /**
     * ��֥��å�ɽ��
     */
    var _updateOddsView = function (autoUpdateOdds){

        if(s.debugMode) console.log('function _updateOddsView');

        $('[id='+s.updateOfficialTimeId+']').text( format_update_time(data['official_datetime']) );

        var odds = data['odds'];
        $('[id^="'+s.oddsUpdatePrefixId+'"]').each(function(){
            var diff_key = $(this).prop('id');
            var tmp_data_key = $(this).attr('id').split('-');
            var data_key = tmp_data_key[1].split('_');
            var type = data_key[0];
            var odds_key = data_key[1];
            var row = odds[type][odds_key];
            var key_ninki_rank = sprintf(s.ninkiUpdatePrefixId+'%1s_%s', type, odds_key);

            if (row) {
                $(this).html(row[0]);
            
                if(s.isBrackets) {
                    $('#'+key_ninki_rank).text( '('+row[2]+')' );
                } else {
                    $('#'+key_ninki_rank).text( row[2] );
                }

                if(s.isDiffValueAnim) {
                    if(!diff_first_flg && !autoUpdateOdds){ //���ʳ�
                        $(this).parents('.'+s.oddsUpdateBackgroundclass).addClass(s.oddsUpdateBackgroundColor);
                    }
                    if(diff_odds[diff_key] != row[0]){
                        diff_odds[diff_key] = row[0];
                        $('[id='+diff_key+']').addClass(s.oddsUpdateColorClass);
                    }
                }
            }
        });
    }

    /**
     * ���ꥪ�å�ɽ��
     */
    var _updateResultOddsView = function (){

        if(s.debugMode) console.log('function _updateResultOddsView');

        var odds = data['odds'];
        $('[id^="'+s.oddsUpdatePrefixId+'"]').each(function(){
            var diff_key = $(this).prop('id');
            var tmp_data_key = $(this).attr('id').split('-');
            var data_key = tmp_data_key[1].split('_');
            var type = data_key[0];
            var odds_key = data_key[1];
            var row = odds[type][odds_key];
            var key_ninki_rank = sprintf(s.ninkiUpdatePrefixId+'%1s_%s', type, odds_key);

            if (row) {
                $(this).html(row[0]);
            
                if(s.isBrackets) {
                    $('#'+key_ninki_rank).text( '('+row[2]+')' );
                } else {
                    $('#'+key_ninki_rank).text( row[2] );
                }

                if(diff_odds[diff_key] != row[0] && s.isDiffValueAnim){
                    diff_odds[diff_key] = row[0];
                    $('[id='+diff_key+']').addClass(s.oddsUpdateColorClass);
                }
            }
        });
    }
    /**
     * @param pattern 1:ͭ��������� 2:��ư�����ܥ���
     * @param update_count 2:��ư�����ܥ���ι������
     */
    var _popupView = function ( pattern, update_count ) {
        if(s.debugMode) console.log('function _popupView');

        $('#premiumm_info').hide();
        $('#free_update_limit').hide();

        if(pattern == '1') {
            $('#premiumm_info').show();//���
        } else if(pattern == '2') {

            var update_limit = s.update_limit - update_count;
            $('#odds_update_rest').html(update_limit);

            if(s.update_limit <= update_count) {
                $('#free_update_limit').show();//���
            }
        }
        $.colorbox( {
            onOpen:function(){
                $("#cboxWrapper").addClass("OddsInfoModal");
            },
            inline: true,
            width: '98%',
            height: '770px',
            maxWidth: '700px',
            transition: "fade",
            reposition: false,
            onComplete: function() {
                $('#OddsInfoSlideBox').slick('refresh');
                setTimeout(function(){
                    $.colorbox.position(0);
                },500);
            },
            href:$('#inline_content'),
        });
    }
    /**
     * �������֤Υե����ޥåȤ��Ѵ�
     *
     * @param new 2018-01-20 15:59:40
     *
     * return 15:59 or 15:59(8ʬ��)  (*ʬ��)�ϸ��߻��狼������л���
     */
    format_update_time = function(new_time) {

if(!new_time){
    new_time = _getDateYmd();
}



        if(s.isPremium == '1' || !s.displayDiffTime) {
            new_time = new_time.replace( /-/g , "/" ) ;
            var date_new = new Date(new_time);
            var h = date_new.getHours();
            var m = date_new.getMinutes();
            var time = sprintf('%s:%02s',h, m);
        } else {
            new_time = new_time.replace( /-/g , "/" ) ;
            var date_new = new Date();
            var date_old = new Date(new_time);
            var new_u_time = Math.floor( date_new.getTime() / 1000 );
            var old_u_time = Math.floor( date_old.getTime() / 1000 );
            var diff_time_min = Math.floor((new_u_time - old_u_time) / 60);
            var h = date_old.getHours();
            var m = date_old.getMinutes();
            var time = sprintf('%s:%02s(%sʬ��)',h, m, diff_time_min);
        }
        return time;
    }

    /**
     *��̵�����������modal���������
     *
     */
    var _getOddsModal = function ( _show_id ) {

        if(s.debugMode) console.log('function _getOddsModal : show_id',_show_id);

        var _data = { pid : 'api_get_odds_modal' };
        _data.input   = 'UTF-8';
        _data.output  = 'jsonp';
        $.ajax( { type     : 'GET',
            url      : '/api/api_get_odds_modal.html',
            data     : _data,
            dataType : _data.output,
            success  : function( data )
            {

                $( '#' + _show_id ).html( data );
            }
        });
    }

    /**
     *  �����������֤�
     */
    var _getDateYmd = function () {
        var now   = new Date();
        var year  = now.getFullYear(); //ǯ
        var month = now.getMonth();    //��
        var day   = now.getDate();     //��
        return sprintf('%04s%02s%02s', year, month, day);
    }

    /**
     * android 4.0.�ʲ��б� lib ZLIB��ư���ʤ��Τǲ�����������å�����
     *
     * �֥饦�� ��� android4.0�ʲ��ξ���false
     */
    var _checkCompress = function() {
       var cookie_name = 'browser_appli[keiba]';
       var appli = getCookie(cookie_name);
       var isCompress = true;
       if(appli) {
           return isCompress;
       }
       var ua = navigator.userAgent.toLowerCase();
       if(ua.indexOf('android') > 0) {
           if(ua.match(/android ([\.\d]+)/)){
               var os_v = RegExp.$1;
               var os_s = os_v.split('.');
               //�ƥ���
               //os_s[0] = '4';
               //os_s[1] = '0';
               //os_s[2] = '4';�ޥ��ʡ��ޥ��ʡ��ޤ�Ƚ�ꤷ�������Ϥ����Ȥ�
               //�ޥ��ʡ��С������ޤǤ�Float���Ѵ�
               var v_major_minor = parseFloat(os_s[0]+'.'+os_s[1]);
               if(4 < v_major_minor) { //4.0����
                   isCompress = true;
               } else { //4.0�ʲ�
                   isCompress = false;
               }
           }
       }
       return isCompress;
    }
})( jQuery );
