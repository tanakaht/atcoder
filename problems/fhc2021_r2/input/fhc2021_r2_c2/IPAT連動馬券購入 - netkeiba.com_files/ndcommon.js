
// $Id: base64.js 145 2017-06-16 07:21:48Z ysimizu $

/* Copyright (C) 1999 Masanao Izumo <iz@onicos.co.jp>
 * Version: 1.0
 * LastModified: Dec 25 1999
 * This library is free.  You can redistribute it and/or modify it.
 * Interfaces:
 * b64 = base64encode(data);
 * data = base64decode(b64);
 */

(function(window) {
    'use strict'

    var base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var base64DecodeChars = new Array(
	    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
	    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
	    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63,
	52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1,
	    -1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
	15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1,
	    -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
	41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1);

    function base64encode(str) {
	var out, i, len;
	var c1, c2, c3;

	len = str.length;
	i = 0;
	out = "";
	while(i < len) {
	    c1 = str.charCodeAt(i++) & 0xff;
	    if(i == len)
	    {
		out += base64EncodeChars.charAt(c1 >> 2);
		out += base64EncodeChars.charAt((c1 & 0x3) << 4);
		out += "==";
		break;
	    }
	    c2 = str.charCodeAt(i++);
	    if(i == len)
	    {
		out += base64EncodeChars.charAt(c1 >> 2);
		out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
		out += base64EncodeChars.charAt((c2 & 0xF) << 2);
		out += "=";
		break;
	    }
	    c3 = str.charCodeAt(i++);
	    out += base64EncodeChars.charAt(c1 >> 2);
	    out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
	    out += base64EncodeChars.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >>6));
	    out += base64EncodeChars.charAt(c3 & 0x3F);
	}
	return out;
    }

    function base64decode(str) {
	var c1, c2, c3, c4;
	var i, len, out;

	len = str.length;
	i = 0;
	out = "";
	while(i < len) {
	    /* c1 */
	    do {
		c1 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
	    } while(i < len && c1 == -1);
	    if(c1 == -1)
		break;

	    /* c2 */
	    do {
		c2 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
	    } while(i < len && c2 == -1);
	    if(c2 == -1)
		break;

	    out += String.fromCharCode((c1 << 2) | ((c2 & 0x30) >> 4));

	    /* c3 */
	    do {
		c3 = str.charCodeAt(i++) & 0xff;
		if(c3 == 61)
		    return out;
		c3 = base64DecodeChars[c3];
	    } while(i < len && c3 == -1);
	    if(c3 == -1)
		break;

	    out += String.fromCharCode(((c2 & 0XF) << 4) | ((c3 & 0x3C) >> 2));

	    /* c4 */
	    do {
		c4 = str.charCodeAt(i++) & 0xff;
		if(c4 == 61)
		    return out;
		c4 = base64DecodeChars[c4];
	    } while(i < len && c4 == -1);
	    if(c4 == -1)
		break;
	    out += String.fromCharCode(((c3 & 0x03) << 6) | c4);
	}
	return out;
    }
    /**
     * export to either browser or node.js
     */
    if (typeof exports !== 'undefined') {
        exports.base64encode = base64encode
        exports.base64decode = base64decode
    }
    else {
        window.base64encode = base64encode
        window.base64decode = base64decode

        if (typeof define === 'function' && define.amd) {
            define(function() {
                return {
                    base64encode: base64encode,
                    base64decode: base64decode
                }
            })
        }
    }
})(typeof window === 'undefined' ? this : window);


(function(){

    var debugMode = false;
    if(undefined !== window.debug_mode){
	debugMode = window.debug_mode;
    }
//    console.log('**** debug_mode: %s',debugMode);
    var methods = [
	'log',
	'debug',
	'info',
	'warn',
	'error',
	'dir',
	'trace',
	'assert',
	'dirxml',
	'group',
	'groupEnd',
	'time',
	'timeEnd',
	'count',
	'profile',
	'profileEnd'
    ];

    if( typeof window.console === "undefined" ){
	window.console = {};
    }
    for( var i in methods ){
	(function( m ){
	    if( console[m] && debugMode && typeof console[m] === "function" ){
		window[m] = function(){ console[m].apply( console, arguments ); };
	    }
	    else{
		window[m] = function(){};
	    }

	})( methods[i] );
    }
})();



/*
 *  $Id: cookie.js 145 2017-06-16 07:21:48Z ysimizu $
 */
(function(window) {
    'use strict'

    // cookieを取得
    function getCookie(cname)
    {
	var name = cname + "=";
	var ca = document.cookie.split(';');
	for(var i = 0; i <ca.length; i++) {
	    var c = ca[i];
	    while (c.charAt(0)==' ') {
		c = c.substring(1);
	    }
	    if (c.indexOf(name) == 0) {
		return c.substring(name.length,c.length);
	    }
	}
	return "";
    }
    // cookieを設定
    function setCookie(cname, cvalue, exdays)
    {
	var d = new Date();
	d.setTime(d.getTime() + (exdays*24*60*60*1000));
	var expires = "expires="+ d.toUTCString();
	document.cookie = cname + "=" + cvalue + "; " + expires;
    }

    /**
     * export to either browser or node.js
     */
    if (typeof exports !== 'undefined') {
        exports.getCookie = getCookie
        exports.setCookie = setCookie
    }
    else {
        window.getCookie = getCookie
        window.setCookie = setCookie

        if (typeof define === 'function' && define.amd) {
            define(function() {
                return {
                    getCookie: getCookie,
                    setCookie: setCookie
                }
            })
        }
    }
    
})(typeof window === 'undefined' ? this : window);




/*
 *  $Id: date_function.js 145 2017-06-16 07:21:48Z ysimizu $
 */

(function(window) {
    'use strict'

    function date_format(date, format)
    {
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
	    for (var i = 0; i < length; i++) format = format.replace(/S/, milliSeconds.substring(i, i + 1));
	}
	return format;
    };
    /**
     * export to either browser or node.js
     */
    if (typeof exports !== 'undefined') {
        exports.date_format = date_format
    }
    else {
        window.date_format = date_format
        if (typeof define === 'function' && define.amd) {
            define(function() {
                return {
                    date_format: date_format,
                }
            })
        }
    }
    
})(typeof window === 'undefined' ? this : window);


/*
	MD5
	Copyright (C) 2007 MITSUNARI Shigeo at Cybozu Labs, Inc.
	license:new BSD license
	how to use
	CybozuLabs.MD5.calc(<ascii string>);
	CybozuLabs.MD5.calc(<unicode(UTF16) string>, CybozuLabs.MD5.BY_UTF16);

	ex. CybozuLabs.MD5.calc("abc") == "900150983cd24fb0d6963f7d28e17f72";
*/
var CybozuLabs = {
	MD5 : {
		// for Firefox
		int2hex8_Fx : function(x) {
			return this.int2hex8((x[1] * 65536) + x[0]);
		},

		update_Fx : function(buf, charSize) {
			var aL = this.a_[0];
			var aH = this.a_[1];
			var bL = this.b_[0];
			var bH = this.b_[1];
			var cL = this.c_[0];
			var cH = this.c_[1];
			var dL = this.d_[0];
			var dH = this.d_[1];
			var tmpL0, tmpL1, tmpL2, tmpL3, tmpL4, tmpL5, tmpL6, tmpL7, tmpL8, tmpL9, tmpLa, tmpLb, tmpLc, tmpLd, tmpLe, tmpLf;
			var tmpH0, tmpH1, tmpH2, tmpH3, tmpH4, tmpH5, tmpH6, tmpH7, tmpH8, tmpH9, tmpHa, tmpHb, tmpHc, tmpHd, tmpHe, tmpHf;
			if (charSize == 1) {
				tmpL0 = buf.charCodeAt( 0) | (buf.charCodeAt( 1) << 8); tmpH0 = buf.charCodeAt( 2) | (buf.charCodeAt( 3) << 8);
				tmpL1 = buf.charCodeAt( 4) | (buf.charCodeAt( 5) << 8); tmpH1 = buf.charCodeAt( 6) | (buf.charCodeAt( 7) << 8);
				tmpL2 = buf.charCodeAt( 8) | (buf.charCodeAt( 9) << 8); tmpH2 = buf.charCodeAt(10) | (buf.charCodeAt(11) << 8);
				tmpL3 = buf.charCodeAt(12) | (buf.charCodeAt(13) << 8); tmpH3 = buf.charCodeAt(14) | (buf.charCodeAt(15) << 8);
				tmpL4 = buf.charCodeAt(16) | (buf.charCodeAt(17) << 8); tmpH4 = buf.charCodeAt(18) | (buf.charCodeAt(19) << 8);
				tmpL5 = buf.charCodeAt(20) | (buf.charCodeAt(21) << 8); tmpH5 = buf.charCodeAt(22) | (buf.charCodeAt(23) << 8);
				tmpL6 = buf.charCodeAt(24) | (buf.charCodeAt(25) << 8); tmpH6 = buf.charCodeAt(26) | (buf.charCodeAt(27) << 8);
				tmpL7 = buf.charCodeAt(28) | (buf.charCodeAt(29) << 8); tmpH7 = buf.charCodeAt(30) | (buf.charCodeAt(31) << 8);
				tmpL8 = buf.charCodeAt(32) | (buf.charCodeAt(33) << 8); tmpH8 = buf.charCodeAt(34) | (buf.charCodeAt(35) << 8);
				tmpL9 = buf.charCodeAt(36) | (buf.charCodeAt(37) << 8); tmpH9 = buf.charCodeAt(38) | (buf.charCodeAt(39) << 8);
				tmpLa = buf.charCodeAt(40) | (buf.charCodeAt(41) << 8); tmpHa = buf.charCodeAt(42) | (buf.charCodeAt(43) << 8);
				tmpLb = buf.charCodeAt(44) | (buf.charCodeAt(45) << 8); tmpHb = buf.charCodeAt(46) | (buf.charCodeAt(47) << 8);
				tmpLc = buf.charCodeAt(48) | (buf.charCodeAt(49) << 8); tmpHc = buf.charCodeAt(50) | (buf.charCodeAt(51) << 8);
				tmpLd = buf.charCodeAt(52) | (buf.charCodeAt(53) << 8); tmpHd = buf.charCodeAt(54) | (buf.charCodeAt(55) << 8);
				tmpLe = buf.charCodeAt(56) | (buf.charCodeAt(57) << 8); tmpHe = buf.charCodeAt(58) | (buf.charCodeAt(59) << 8);
				tmpLf = buf.charCodeAt(60) | (buf.charCodeAt(61) << 8); tmpHf = buf.charCodeAt(62) | (buf.charCodeAt(63) << 8);
			} else {
				tmpL0 = buf.charCodeAt( 0); tmpH0 = buf.charCodeAt( 1);
				tmpL1 = buf.charCodeAt( 2); tmpH1 = buf.charCodeAt( 3);
				tmpL2 = buf.charCodeAt( 4); tmpH2 = buf.charCodeAt( 5);
				tmpL3 = buf.charCodeAt( 6); tmpH3 = buf.charCodeAt( 7);
				tmpL4 = buf.charCodeAt( 8); tmpH4 = buf.charCodeAt( 9);
				tmpL5 = buf.charCodeAt(10); tmpH5 = buf.charCodeAt(11);
				tmpL6 = buf.charCodeAt(12); tmpH6 = buf.charCodeAt(13);
				tmpL7 = buf.charCodeAt(14); tmpH7 = buf.charCodeAt(15);
				tmpL8 = buf.charCodeAt(16); tmpH8 = buf.charCodeAt(17);
				tmpL9 = buf.charCodeAt(18); tmpH9 = buf.charCodeAt(19);
				tmpLa = buf.charCodeAt(20); tmpHa = buf.charCodeAt(21);
				tmpLb = buf.charCodeAt(22); tmpHb = buf.charCodeAt(23);
				tmpLc = buf.charCodeAt(24); tmpHc = buf.charCodeAt(25);
				tmpLd = buf.charCodeAt(26); tmpHd = buf.charCodeAt(27);
				tmpLe = buf.charCodeAt(28); tmpHe = buf.charCodeAt(29);
				tmpLf = buf.charCodeAt(30); tmpHf = buf.charCodeAt(31);
			}

			var t;
			aL += ((bL & cL) | (~bL & dL)) + tmpL0 + 0xa478; aH += ((bH & cH) | (~bH & dH)) + tmpH0 + 0xd76a;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >>  9) | ((aL <<  7) & 65535); aH = (aL >>  9) | ((aH <<  7) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL & bL) | (~aL & cL)) + tmpL1 + 0xb756; dH += ((aH & bH) | (~aH & cH)) + tmpH1 + 0xe8c7;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  4) | ((dL << 12) & 65535); dH = (dL >>  4) | ((dH << 12) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL & aL) | (~dL & bL)) + tmpL2 + 0x70db; cH += ((dH & aH) | (~dH & bH)) + tmpH2 + 0x2420;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cL >> 15) | ((cH <<  1) & 65535); cH = (cH >> 15) | ((cL <<  1) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL & dL) | (~cL & aL)) + tmpL3 + 0xceee; bH += ((cH & dH) | (~cH & aH)) + tmpH3 + 0xc1bd;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 10) | ((bH <<  6) & 65535); bH = (bH >> 10) | ((bL <<  6) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += ((bL & cL) | (~bL & dL)) + tmpL4 + 0x0faf; aH += ((bH & cH) | (~bH & dH)) + tmpH4 + 0xf57c;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >>  9) | ((aL <<  7) & 65535); aH = (aL >>  9) | ((aH <<  7) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL & bL) | (~aL & cL)) + tmpL5 + 0xc62a; dH += ((aH & bH) | (~aH & cH)) + tmpH5 + 0x4787;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  4) | ((dL << 12) & 65535); dH = (dL >>  4) | ((dH << 12) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL & aL) | (~dL & bL)) + tmpL6 + 0x4613; cH += ((dH & aH) | (~dH & bH)) + tmpH6 + 0xa830;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cL >> 15) | ((cH <<  1) & 65535); cH = (cH >> 15) | ((cL <<  1) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL & dL) | (~cL & aL)) + tmpL7 + 0x9501; bH += ((cH & dH) | (~cH & aH)) + tmpH7 + 0xfd46;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 10) | ((bH <<  6) & 65535); bH = (bH >> 10) | ((bL <<  6) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += ((bL & cL) | (~bL & dL)) + tmpL8 + 0x98d8; aH += ((bH & cH) | (~bH & dH)) + tmpH8 + 0x6980;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >>  9) | ((aL <<  7) & 65535); aH = (aL >>  9) | ((aH <<  7) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL & bL) | (~aL & cL)) + tmpL9 + 0xf7af; dH += ((aH & bH) | (~aH & cH)) + tmpH9 + 0x8b44;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  4) | ((dL << 12) & 65535); dH = (dL >>  4) | ((dH << 12) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL & aL) | (~dL & bL)) + tmpLa + 0x5bb1; cH += ((dH & aH) | (~dH & bH)) + tmpHa + 0xffff;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cL >> 15) | ((cH <<  1) & 65535); cH = (cH >> 15) | ((cL <<  1) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL & dL) | (~cL & aL)) + tmpLb + 0xd7be; bH += ((cH & dH) | (~cH & aH)) + tmpHb + 0x895c;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 10) | ((bH <<  6) & 65535); bH = (bH >> 10) | ((bL <<  6) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += ((bL & cL) | (~bL & dL)) + tmpLc + 0x1122; aH += ((bH & cH) | (~bH & dH)) + tmpHc + 0x6b90;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >>  9) | ((aL <<  7) & 65535); aH = (aL >>  9) | ((aH <<  7) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL & bL) | (~aL & cL)) + tmpLd + 0x7193; dH += ((aH & bH) | (~aH & cH)) + tmpHd + 0xfd98;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  4) | ((dL << 12) & 65535); dH = (dL >>  4) | ((dH << 12) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL & aL) | (~dL & bL)) + tmpLe + 0x438e; cH += ((dH & aH) | (~dH & bH)) + tmpHe + 0xa679;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cL >> 15) | ((cH <<  1) & 65535); cH = (cH >> 15) | ((cL <<  1) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL & dL) | (~cL & aL)) + tmpLf + 0x0821; bH += ((cH & dH) | (~cH & aH)) + tmpHf + 0x49b4;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 10) | ((bH <<  6) & 65535); bH = (bH >> 10) | ((bL <<  6) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
///
			aL += ((bL & dL) | (cL & ~dL)) + tmpL1 + 0x2562; aH += ((bH & dH) | (cH & ~dH)) + tmpH1 + 0xf61e;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 11) | ((aL <<  5) & 65535); aH = (aL >> 11) | ((aH <<  5) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL & cL) | (bL & ~cL)) + tmpL6 + 0xb340; dH += ((aH & cH) | (bH & ~cH)) + tmpH6 + 0xc040;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  7) | ((dL <<  9) & 65535); dH = (dL >>  7) | ((dH <<  9) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL & bL) | (aL & ~bL)) + tmpLb + 0x5a51; cH += ((dH & bH) | (aH & ~bH)) + tmpHb + 0x265e;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cH >>  2) | ((cL << 14) & 65535); cH = (cL >>  2) | ((cH << 14) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL & aL) | (dL & ~aL)) + tmpL0 + 0xc7aa; bH += ((cH & aH) | (dH & ~aH)) + tmpH0 + 0xe9b6;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 12) | ((bH <<  4) & 65535); bH = (bH >> 12) | ((bL <<  4) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += ((bL & dL) | (cL & ~dL)) + tmpL5 + 0x105d; aH += ((bH & dH) | (cH & ~dH)) + tmpH5 + 0xd62f;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 11) | ((aL <<  5) & 65535); aH = (aL >> 11) | ((aH <<  5) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL & cL) | (bL & ~cL)) + tmpLa + 0x1453; dH += ((aH & cH) | (bH & ~cH)) + tmpHa + 0x0244;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  7) | ((dL <<  9) & 65535); dH = (dL >>  7) | ((dH <<  9) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL & bL) | (aL & ~bL)) + tmpLf + 0xe681; cH += ((dH & bH) | (aH & ~bH)) + tmpHf + 0xd8a1;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cH >>  2) | ((cL << 14) & 65535); cH = (cL >>  2) | ((cH << 14) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL & aL) | (dL & ~aL)) + tmpL4 + 0xfbc8; bH += ((cH & aH) | (dH & ~aH)) + tmpH4 + 0xe7d3;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 12) | ((bH <<  4) & 65535); bH = (bH >> 12) | ((bL <<  4) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += ((bL & dL) | (cL & ~dL)) + tmpL9 + 0xcde6; aH += ((bH & dH) | (cH & ~dH)) + tmpH9 + 0x21e1;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 11) | ((aL <<  5) & 65535); aH = (aL >> 11) | ((aH <<  5) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL & cL) | (bL & ~cL)) + tmpLe + 0x07d6; dH += ((aH & cH) | (bH & ~cH)) + tmpHe + 0xc337;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  7) | ((dL <<  9) & 65535); dH = (dL >>  7) | ((dH <<  9) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL & bL) | (aL & ~bL)) + tmpL3 + 0x0d87; cH += ((dH & bH) | (aH & ~bH)) + tmpH3 + 0xf4d5;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cH >>  2) | ((cL << 14) & 65535); cH = (cL >>  2) | ((cH << 14) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL & aL) | (dL & ~aL)) + tmpL8 + 0x14ed; bH += ((cH & aH) | (dH & ~aH)) + tmpH8 + 0x455a;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 12) | ((bH <<  4) & 65535); bH = (bH >> 12) | ((bL <<  4) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += ((bL & dL) | (cL & ~dL)) + tmpLd + 0xe905; aH += ((bH & dH) | (cH & ~dH)) + tmpHd + 0xa9e3;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 11) | ((aL <<  5) & 65535); aH = (aL >> 11) | ((aH <<  5) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL & cL) | (bL & ~cL)) + tmpL2 + 0xa3f8; dH += ((aH & cH) | (bH & ~cH)) + tmpH2 + 0xfcef;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  7) | ((dL <<  9) & 65535); dH = (dL >>  7) | ((dH <<  9) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL & bL) | (aL & ~bL)) + tmpL7 + 0x02d9; cH += ((dH & bH) | (aH & ~bH)) + tmpH7 + 0x676f;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cH >>  2) | ((cL << 14) & 65535); cH = (cL >>  2) | ((cH << 14) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL & aL) | (dL & ~aL)) + tmpLc + 0x4c8a; bH += ((cH & aH) | (dH & ~aH)) + tmpHc + 0x8d2a;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 12) | ((bH <<  4) & 65535); bH = (bH >> 12) | ((bL <<  4) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
///
			aL += ((bL ^ cL) ^ dL) + tmpL5 + 0x3942; aH += ((bH ^ cH) ^ dH) + tmpH5 + 0xfffa;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 12) | ((aL <<  4) & 65535); aH = (aL >> 12) | ((aH <<  4) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL ^ bL) ^ cL) + tmpL8 + 0xf681; dH += ((aH ^ bH) ^ cH) + tmpH8 + 0x8771;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  5) | ((dL << 11) & 65535); dH = (dL >>  5) | ((dH << 11) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL ^ aL) ^ bL) + tmpLb + 0x6122; cH += ((dH ^ aH) ^ bH) + tmpHb + 0x6d9d;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cL >> 16) | ((cH <<  0) & 65535); cH = (cH >> 16) | ((cL <<  0) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL ^ dL) ^ aL) + tmpLe + 0x380c; bH += ((cH ^ dH) ^ aH) + tmpHe + 0xfde5;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >>  9) | ((bH <<  7) & 65535); bH = (bH >>  9) | ((bL <<  7) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += ((bL ^ cL) ^ dL) + tmpL1 + 0xea44; aH += ((bH ^ cH) ^ dH) + tmpH1 + 0xa4be;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 12) | ((aL <<  4) & 65535); aH = (aL >> 12) | ((aH <<  4) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL ^ bL) ^ cL) + tmpL4 + 0xcfa9; dH += ((aH ^ bH) ^ cH) + tmpH4 + 0x4bde;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  5) | ((dL << 11) & 65535); dH = (dL >>  5) | ((dH << 11) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL ^ aL) ^ bL) + tmpL7 + 0x4b60; cH += ((dH ^ aH) ^ bH) + tmpH7 + 0xf6bb;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cL >> 16) | ((cH <<  0) & 65535); cH = (cH >> 16) | ((cL <<  0) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL ^ dL) ^ aL) + tmpLa + 0xbc70; bH += ((cH ^ dH) ^ aH) + tmpHa + 0xbebf;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >>  9) | ((bH <<  7) & 65535); bH = (bH >>  9) | ((bL <<  7) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += ((bL ^ cL) ^ dL) + tmpLd + 0x7ec6; aH += ((bH ^ cH) ^ dH) + tmpHd + 0x289b;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 12) | ((aL <<  4) & 65535); aH = (aL >> 12) | ((aH <<  4) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL ^ bL) ^ cL) + tmpL0 + 0x27fa; dH += ((aH ^ bH) ^ cH) + tmpH0 + 0xeaa1;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  5) | ((dL << 11) & 65535); dH = (dL >>  5) | ((dH << 11) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL ^ aL) ^ bL) + tmpL3 + 0x3085; cH += ((dH ^ aH) ^ bH) + tmpH3 + 0xd4ef;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cL >> 16) | ((cH <<  0) & 65535); cH = (cH >> 16) | ((cL <<  0) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL ^ dL) ^ aL) + tmpL6 + 0x1d05; bH += ((cH ^ dH) ^ aH) + tmpH6 + 0x0488;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >>  9) | ((bH <<  7) & 65535); bH = (bH >>  9) | ((bL <<  7) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += ((bL ^ cL) ^ dL) + tmpL9 + 0xd039; aH += ((bH ^ cH) ^ dH) + tmpH9 + 0xd9d4;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 12) | ((aL <<  4) & 65535); aH = (aL >> 12) | ((aH <<  4) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += ((aL ^ bL) ^ cL) + tmpLc + 0x99e5; dH += ((aH ^ bH) ^ cH) + tmpHc + 0xe6db;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  5) | ((dL << 11) & 65535); dH = (dL >>  5) | ((dH << 11) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += ((dL ^ aL) ^ bL) + tmpLf + 0x7cf8; cH += ((dH ^ aH) ^ bH) + tmpHf + 0x1fa2;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cL >> 16) | ((cH <<  0) & 65535); cH = (cH >> 16) | ((cL <<  0) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += ((cL ^ dL) ^ aL) + tmpL2 + 0x5665; bH += ((cH ^ dH) ^ aH) + tmpH2 + 0xc4ac;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >>  9) | ((bH <<  7) & 65535); bH = (bH >>  9) | ((bL <<  7) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
///
			aL += (cL ^ ((65535 - dL) | bL)) + tmpL0 + 0x2244; aH += (cH ^ ((65535 - dH) | bH)) + tmpH0 + 0xf429;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 10) | ((aL <<  6) & 65535); aH = (aL >> 10) | ((aH <<  6) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += (bL ^ ((65535 - cL) | aL)) + tmpL7 + 0xff97; dH += (bH ^ ((65535 - cH) | aH)) + tmpH7 + 0x432a;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  6) | ((dL << 10) & 65535); dH = (dL >>  6) | ((dH << 10) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += (aL ^ ((65535 - bL) | dL)) + tmpLe + 0x23a7; cH += (aH ^ ((65535 - bH) | dH)) + tmpHe + 0xab94;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cH >>  1) | ((cL << 15) & 65535); cH = (cL >>  1) | ((cH << 15) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += (dL ^ ((65535 - aL) | cL)) + tmpL5 + 0xa039; bH += (dH ^ ((65535 - aH) | cH)) + tmpH5 + 0xfc93;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 11) | ((bH <<  5) & 65535); bH = (bH >> 11) | ((bL <<  5) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += (cL ^ ((65535 - dL) | bL)) + tmpLc + 0x59c3; aH += (cH ^ ((65535 - dH) | bH)) + tmpHc + 0x655b;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 10) | ((aL <<  6) & 65535); aH = (aL >> 10) | ((aH <<  6) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += (bL ^ ((65535 - cL) | aL)) + tmpL3 + 0xcc92; dH += (bH ^ ((65535 - cH) | aH)) + tmpH3 + 0x8f0c;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  6) | ((dL << 10) & 65535); dH = (dL >>  6) | ((dH << 10) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += (aL ^ ((65535 - bL) | dL)) + tmpLa + 0xf47d; cH += (aH ^ ((65535 - bH) | dH)) + tmpHa + 0xffef;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cH >>  1) | ((cL << 15) & 65535); cH = (cL >>  1) | ((cH << 15) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += (dL ^ ((65535 - aL) | cL)) + tmpL1 + 0x5dd1; bH += (dH ^ ((65535 - aH) | cH)) + tmpH1 + 0x8584;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 11) | ((bH <<  5) & 65535); bH = (bH >> 11) | ((bL <<  5) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += (cL ^ ((65535 - dL) | bL)) + tmpL8 + 0x7e4f; aH += (cH ^ ((65535 - dH) | bH)) + tmpH8 + 0x6fa8;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 10) | ((aL <<  6) & 65535); aH = (aL >> 10) | ((aH <<  6) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += (bL ^ ((65535 - cL) | aL)) + tmpLf + 0xe6e0; dH += (bH ^ ((65535 - cH) | aH)) + tmpHf + 0xfe2c;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  6) | ((dL << 10) & 65535); dH = (dL >>  6) | ((dH << 10) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += (aL ^ ((65535 - bL) | dL)) + tmpL6 + 0x4314; cH += (aH ^ ((65535 - bH) | dH)) + tmpH6 + 0xa301;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cH >>  1) | ((cL << 15) & 65535); cH = (cL >>  1) | ((cH << 15) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += (dL ^ ((65535 - aL) | cL)) + tmpLd + 0x11a1; bH += (dH ^ ((65535 - aH) | cH)) + tmpHd + 0x4e08;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 11) | ((bH <<  5) & 65535); bH = (bH >> 11) | ((bL <<  5) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
			aL += (cL ^ ((65535 - dL) | bL)) + tmpL4 + 0x7e82; aH += (cH ^ ((65535 - dH) | bH)) + tmpH4 + 0xf753;
			aH += aL >> 16;
			aL &= 65535; aH &= 65535;
			t = (aH >> 10) | ((aL <<  6) & 65535); aH = (aL >> 10) | ((aH <<  6) & 65535);
			aL = t + bL; aH += bH; if (aL > 65535) { aL &= 65535; aH++; }
			aH &= 65535;
			dL += (bL ^ ((65535 - cL) | aL)) + tmpLb + 0xf235; dH += (bH ^ ((65535 - cH) | aH)) + tmpHb + 0xbd3a;
			dH += dL >> 16;
			dL &= 65535; dH &= 65535;
			t = (dH >>  6) | ((dL << 10) & 65535); dH = (dL >>  6) | ((dH << 10) & 65535);
			dL = t + aL; dH += aH; if (dL > 65535) { dL &= 65535; dH++; }
			dH &= 65535;
			cL += (aL ^ ((65535 - bL) | dL)) + tmpL2 + 0xd2bb; cH += (aH ^ ((65535 - bH) | dH)) + tmpH2 + 0x2ad7;
			cH += cL >> 16;
			cL &= 65535; cH &= 65535;
			t = (cH >>  1) | ((cL << 15) & 65535); cH = (cL >>  1) | ((cH << 15) & 65535);
			cL = t + dL; cH += dH; if (cL > 65535) { cL &= 65535; cH++; }
			cH &= 65535;
			bL += (dL ^ ((65535 - aL) | cL)) + tmpL9 + 0xd391; bH += (dH ^ ((65535 - aH) | cH)) + tmpH9 + 0xeb86;
			bH += bL >> 16;
			bL &= 65535; bH &= 65535;
			t = (bL >> 11) | ((bH <<  5) & 65535); bH = (bH >> 11) | ((bL <<  5) & 65535);
			bL = t + cL; bH += cH; if (bL > 65535) { bL &= 65535; bH++; }
			bH &= 65535;
///
			t = this.a_[0] += aL; this.a_[1] += aH; if (t > 65535) { this.a_[0] -= 65536; this.a_[1]++; } this.a_[1] &= 65535;
			t = this.b_[0] += bL; this.b_[1] += bH; if (t > 65535) { this.b_[0] -= 65536; this.b_[1]++; } this.b_[1] &= 65535;
			t = this.c_[0] += cL; this.c_[1] += cH; if (t > 65535) { this.c_[0] -= 65536; this.c_[1]++; } this.c_[1] &= 65535;
			t = this.d_[0] += dL; this.d_[1] += dH; if (t > 65535) { this.d_[0] -= 65536; this.d_[1]++; } this.d_[1] &= 65535;
		},

		/* sprintf(buf, "%08x", i32); */
		int2hex8 : function(i32) {
			var i, c, ret = "";
			var hex = "0123456789abcdef";
			for (i = 0; i < 4; i++) {
				c = i32 >>> (i * 8);
				ret += hex.charAt((c >> 4) & 15);
				ret += hex.charAt(c & 15);
			}
			return ret;
		},

		update_std : function(buf, charSize) {
			var a = this.a_, b = this.b_, c = this.c_, d = this.d_;
			var tmp0, tmp1, tmp2, tmp3, tmp4, tmp5, tmp6, tmp7, tmp8, tmp9, tmpa, tmpb, tmpc, tmpd, tmpe, tmpf;
			if (charSize == 1) {
				tmp0 = buf.charCodeAt( 0) | (buf.charCodeAt( 1) << 8) | (buf.charCodeAt( 2) << 16) | (buf.charCodeAt( 3) << 24);
				tmp1 = buf.charCodeAt( 4) | (buf.charCodeAt( 5) << 8) | (buf.charCodeAt( 6) << 16) | (buf.charCodeAt( 7) << 24);
				tmp2 = buf.charCodeAt( 8) | (buf.charCodeAt( 9) << 8) | (buf.charCodeAt(10) << 16) | (buf.charCodeAt(11) << 24);
				tmp3 = buf.charCodeAt(12) | (buf.charCodeAt(13) << 8) | (buf.charCodeAt(14) << 16) | (buf.charCodeAt(15) << 24);
				tmp4 = buf.charCodeAt(16) | (buf.charCodeAt(17) << 8) | (buf.charCodeAt(18) << 16) | (buf.charCodeAt(19) << 24);
				tmp5 = buf.charCodeAt(20) | (buf.charCodeAt(21) << 8) | (buf.charCodeAt(22) << 16) | (buf.charCodeAt(23) << 24);
				tmp6 = buf.charCodeAt(24) | (buf.charCodeAt(25) << 8) | (buf.charCodeAt(26) << 16) | (buf.charCodeAt(27) << 24);
				tmp7 = buf.charCodeAt(28) | (buf.charCodeAt(29) << 8) | (buf.charCodeAt(30) << 16) | (buf.charCodeAt(31) << 24);
				tmp8 = buf.charCodeAt(32) | (buf.charCodeAt(33) << 8) | (buf.charCodeAt(34) << 16) | (buf.charCodeAt(35) << 24);
				tmp9 = buf.charCodeAt(36) | (buf.charCodeAt(37) << 8) | (buf.charCodeAt(38) << 16) | (buf.charCodeAt(39) << 24);
				tmpa = buf.charCodeAt(40) | (buf.charCodeAt(41) << 8) | (buf.charCodeAt(42) << 16) | (buf.charCodeAt(43) << 24);
				tmpb = buf.charCodeAt(44) | (buf.charCodeAt(45) << 8) | (buf.charCodeAt(46) << 16) | (buf.charCodeAt(47) << 24);
				tmpc = buf.charCodeAt(48) | (buf.charCodeAt(49) << 8) | (buf.charCodeAt(50) << 16) | (buf.charCodeAt(51) << 24);
				tmpd = buf.charCodeAt(52) | (buf.charCodeAt(53) << 8) | (buf.charCodeAt(54) << 16) | (buf.charCodeAt(55) << 24);
				tmpe = buf.charCodeAt(56) | (buf.charCodeAt(57) << 8) | (buf.charCodeAt(58) << 16) | (buf.charCodeAt(59) << 24);
				tmpf = buf.charCodeAt(60) | (buf.charCodeAt(61) << 8) | (buf.charCodeAt(62) << 16) | (buf.charCodeAt(63) << 24);
			} else {
				tmp0 = buf.charCodeAt( 0) | (buf.charCodeAt( 1) << 16);
				tmp1 = buf.charCodeAt( 2) | (buf.charCodeAt( 3) << 16);
				tmp2 = buf.charCodeAt( 4) | (buf.charCodeAt( 5) << 16);
				tmp3 = buf.charCodeAt( 6) | (buf.charCodeAt( 7) << 16);
				tmp4 = buf.charCodeAt( 8) | (buf.charCodeAt( 9) << 16);
				tmp5 = buf.charCodeAt(10) | (buf.charCodeAt(11) << 16);
				tmp6 = buf.charCodeAt(12) | (buf.charCodeAt(13) << 16);
				tmp7 = buf.charCodeAt(14) | (buf.charCodeAt(15) << 16);
				tmp8 = buf.charCodeAt(16) | (buf.charCodeAt(17) << 16);
				tmp9 = buf.charCodeAt(18) | (buf.charCodeAt(19) << 16);
				tmpa = buf.charCodeAt(20) | (buf.charCodeAt(21) << 16);
				tmpb = buf.charCodeAt(22) | (buf.charCodeAt(23) << 16);
				tmpc = buf.charCodeAt(24) | (buf.charCodeAt(25) << 16);
				tmpd = buf.charCodeAt(26) | (buf.charCodeAt(27) << 16);
				tmpe = buf.charCodeAt(28) | (buf.charCodeAt(29) << 16);
				tmpf = buf.charCodeAt(30) | (buf.charCodeAt(31) << 16);
			}

			a += tmp0 + 0xd76aa478 + ((b & c) | (~b & d)); a = b + ((a <<  7) | (a >>> 25));
			d += tmp1 + 0xe8c7b756 + ((a & b) | (~a & c)); d = a + ((d << 12) | (d >>> 20));
			c += tmp2 + 0x242070db + ((d & a) | (~d & b)); c = d + ((c << 17) | (c >>> 15));
			b += tmp3 + 0xc1bdceee + ((c & d) | (~c & a)); b = c + ((b << 22) | (b >>> 10));
			a += tmp4 + 0xf57c0faf + ((b & c) | (~b & d)); a = b + ((a <<  7) | (a >>> 25));
			d += tmp5 + 0x4787c62a + ((a & b) | (~a & c)); d = a + ((d << 12) | (d >>> 20));
			c += tmp6 + 0xa8304613 + ((d & a) | (~d & b)); c = d + ((c << 17) | (c >>> 15));
			b += tmp7 + 0xfd469501 + ((c & d) | (~c & a)); b = c + ((b << 22) | (b >>> 10));
			a += tmp8 + 0x698098d8 + ((b & c) | (~b & d)); a = b + ((a <<  7) | (a >>> 25));
			d += tmp9 + 0x8b44f7af + ((a & b) | (~a & c)); d = a + ((d << 12) | (d >>> 20));
			c += tmpa + 0xffff5bb1 + ((d & a) | (~d & b)); c = d + ((c << 17) | (c >>> 15));
			b += tmpb + 0x895cd7be + ((c & d) | (~c & a)); b = c + ((b << 22) | (b >>> 10));
			a += tmpc + 0x6b901122 + ((b & c) | (~b & d)); a = b + ((a <<  7) | (a >>> 25));
			d += tmpd + 0xfd987193 + ((a & b) | (~a & c)); d = a + ((d << 12) | (d >>> 20));
			c += tmpe + 0xa679438e + ((d & a) | (~d & b)); c = d + ((c << 17) | (c >>> 15));
			b += tmpf + 0x49b40821 + ((c & d) | (~c & a)); b = c + ((b << 22) | (b >>> 10));
			a += tmp1 + 0xf61e2562 + ((b & d) | (c & ~d)); a = b + ((a <<  5) | (a >>> 27));
			d += tmp6 + 0xc040b340 + ((a & c) | (b & ~c)); d = a + ((d <<  9) | (d >>> 23));
			c += tmpb + 0x265e5a51 + ((d & b) | (a & ~b)); c = d + ((c << 14) | (c >>> 18));
			b += tmp0 + 0xe9b6c7aa + ((c & a) | (d & ~a)); b = c + ((b << 20) | (b >>> 12));
			a += tmp5 + 0xd62f105d + ((b & d) | (c & ~d)); a = b + ((a <<  5) | (a >>> 27));
			d += tmpa + 0x02441453 + ((a & c) | (b & ~c)); d = a + ((d <<  9) | (d >>> 23));
			c += tmpf + 0xd8a1e681 + ((d & b) | (a & ~b)); c = d + ((c << 14) | (c >>> 18));
			b += tmp4 + 0xe7d3fbc8 + ((c & a) | (d & ~a)); b = c + ((b << 20) | (b >>> 12));
			a += tmp9 + 0x21e1cde6 + ((b & d) | (c & ~d)); a = b + ((a <<  5) | (a >>> 27));
			d += tmpe + 0xc33707d6 + ((a & c) | (b & ~c)); d = a + ((d <<  9) | (d >>> 23));
			c += tmp3 + 0xf4d50d87 + ((d & b) | (a & ~b)); c = d + ((c << 14) | (c >>> 18));
			b += tmp8 + 0x455a14ed + ((c & a) | (d & ~a)); b = c + ((b << 20) | (b >>> 12));
			a += tmpd + 0xa9e3e905 + ((b & d) | (c & ~d)); a = b + ((a <<  5) | (a >>> 27));
			d += tmp2 + 0xfcefa3f8 + ((a & c) | (b & ~c)); d = a + ((d <<  9) | (d >>> 23));
			c += tmp7 + 0x676f02d9 + ((d & b) | (a & ~b)); c = d + ((c << 14) | (c >>> 18));
			b += tmpc + 0x8d2a4c8a + ((c & a) | (d & ~a)); b = c + ((b << 20) | (b >>> 12));
			a += tmp5 + 0xfffa3942 + ((b ^ c) ^ d); a = b + ((a <<  4) | (a >>> 28));
			d += tmp8 + 0x8771f681 + ((a ^ b) ^ c); d = a + ((d << 11) | (d >>> 21));
			c += tmpb + 0x6d9d6122 + ((d ^ a) ^ b); c = d + ((c << 16) | (c >>> 16));
			b += tmpe + 0xfde5380c + ((c ^ d) ^ a); b = c + ((b << 23) | (b >>>  9));
			a += tmp1 + 0xa4beea44 + ((b ^ c) ^ d); a = b + ((a <<  4) | (a >>> 28));
			d += tmp4 + 0x4bdecfa9 + ((a ^ b) ^ c); d = a + ((d << 11) | (d >>> 21));
			c += tmp7 + 0xf6bb4b60 + ((d ^ a) ^ b); c = d + ((c << 16) | (c >>> 16));
			b += tmpa + 0xbebfbc70 + ((c ^ d) ^ a); b = c + ((b << 23) | (b >>>  9));
			a += tmpd + 0x289b7ec6 + ((b ^ c) ^ d); a = b + ((a <<  4) | (a >>> 28));
			d += tmp0 + 0xeaa127fa + ((a ^ b) ^ c); d = a + ((d << 11) | (d >>> 21));
			c += tmp3 + 0xd4ef3085 + ((d ^ a) ^ b); c = d + ((c << 16) | (c >>> 16));
			b += tmp6 + 0x04881d05 + ((c ^ d) ^ a); b = c + ((b << 23) | (b >>>  9));
			a += tmp9 + 0xd9d4d039 + ((b ^ c) ^ d); a = b + ((a <<  4) | (a >>> 28));
			d += tmpc + 0xe6db99e5 + ((a ^ b) ^ c); d = a + ((d << 11) | (d >>> 21));
			c += tmpf + 0x1fa27cf8 + ((d ^ a) ^ b); c = d + ((c << 16) | (c >>> 16));
			b += tmp2 + 0xc4ac5665 + ((c ^ d) ^ a); b = c + ((b << 23) | (b >>>  9));
			a += tmp0 + 0xf4292244 + (c ^ (~d | b)); a = b + ((a <<  6) | (a >>> 26));
			d += tmp7 + 0x432aff97 + (b ^ (~c | a)); d = a + ((d << 10) | (d >>> 22));
			c += tmpe + 0xab9423a7 + (a ^ (~b | d)); c = d + ((c << 15) | (c >>> 17));
			b += tmp5 + 0xfc93a039 + (d ^ (~a | c)); b = c + ((b << 21) | (b >>> 11));
			a += tmpc + 0x655b59c3 + (c ^ (~d | b)); a = b + ((a <<  6) | (a >>> 26));
			d += tmp3 + 0x8f0ccc92 + (b ^ (~c | a)); d = a + ((d << 10) | (d >>> 22));
			c += tmpa + 0xffeff47d + (a ^ (~b | d)); c = d + ((c << 15) | (c >>> 17));
			b += tmp1 + 0x85845dd1 + (d ^ (~a | c)); b = c + ((b << 21) | (b >>> 11));
			a += tmp8 + 0x6fa87e4f + (c ^ (~d | b)); a = b + ((a <<  6) | (a >>> 26));
			d += tmpf + 0xfe2ce6e0 + (b ^ (~c | a)); d = a + ((d << 10) | (d >>> 22));
			c += tmp6 + 0xa3014314 + (a ^ (~b | d)); c = d + ((c << 15) | (c >>> 17));
			b += tmpd + 0x4e0811a1 + (d ^ (~a | c)); b = c + ((b << 21) | (b >>> 11));
			a += tmp4 + 0xf7537e82 + (c ^ (~d | b)); a = b + ((a <<  6) | (a >>> 26));
			d += tmpb + 0xbd3af235 + (b ^ (~c | a)); d = a + ((d << 10) | (d >>> 22));
			c += tmp2 + 0x2ad7d2bb + (a ^ (~b | d)); c = d + ((c << 15) | (c >>> 17));
			b += tmp9 + 0xeb86d391 + (d ^ (~a | c)); b = c + ((b << 21) | (b >>> 11));

			this.a_ = (this.a_ + a) & 0xffffffff;
			this.b_ = (this.b_ + b) & 0xffffffff;
			this.c_ = (this.c_ + c) & 0xffffffff;
			this.d_ = (this.d_ + d) & 0xffffffff;
		},

		fillzero : function(size) {
			var buf = "";
			for (var i = 0; i < size; i++) {
				buf += "\x00";
			}
			return buf;
		},

		main : function(buf, bufSize, update, self, charSize) {
			if (charSize == 1) {
				var totalBitSize = bufSize * 8;
				while (bufSize >= 64) {
					self[update](buf, charSize);
					buf = buf.substr(64);
					bufSize -= 64;
				}
				buf +="\x80";
				if (bufSize >= 56) {
					buf += this.fillzero(63 - bufSize);
					self[update](buf, charSize);
					buf = this.fillzero(56);
				} else {
					buf += this.fillzero(55 - bufSize);
				}
				buf += String.fromCharCode(totalBitSize & 0xff, (totalBitSize >>> 8) & 0xff, (totalBitSize >>> 16) & 0xff, totalBitSize >>> 24);
				buf += "\x00\x00\x00\x00"; // in stead of (totalBitSize) >> 32
				self[update](buf, charSize);
			} else {
				/* charSize == 2 */
				var totalBitSize = bufSize * 16;
				while (bufSize >= 32) {
					self[update](buf, charSize);
					buf = buf.substr(32);
					bufSize -= 32;
				}
				buf +="\x80";
				if (bufSize >= 28) {
					buf += this.fillzero(31 - bufSize);
					self[update](buf, charSize);
					buf = this.fillzero(28);
				} else {
					buf += this.fillzero(27 - bufSize);
				}
				buf += String.fromCharCode(totalBitSize & 0xffff, totalBitSize >>> 16);
				buf += "\x00\x00"; // in stead of (totalBitSize) >> 32
				self[update](buf, charSize);
			}
		},

		VERSION : "1.0",
		BY_ASCII : 0,
		BY_UTF16 : 1,

		calc_Fx : function(msg, mode) {
			var charSize = (arguments.length == 2 && mode == this.BY_UTF16) ? 2 : 1;
			this.a_ = [0x2301, 0x6745];
			this.b_ = [0xab89, 0xefcd];
			this.c_ = [0xdcfe, 0x98ba];
			this.d_ = [0x5476, 0x1032];
			this.main(msg, msg.length, "update_Fx", this, charSize);
			return this.int2hex8_Fx(this.a_) + this.int2hex8_Fx(this.b_) + this.int2hex8_Fx(this.c_) + this.int2hex8_Fx(this.d_);
		},

		calc_std : function(msg, mode) {
			var charSize = (arguments.length == 2 && mode == this.BY_UTF16) ? 2 : 1;
			this.a_ = 0x67452301;
			this.b_ = 0xefcdab89;
			this.c_ = 0x98badcfe;
			this.d_ = 0x10325476;
			this.main(msg, msg.length, "update_std", this, charSize);
			return this.int2hex8(this.a_) + this.int2hex8(this.b_) + this.int2hex8(this.c_) + this.int2hex8(this.d_);
		}
	} // end of MD5
}; // end of CybozuLabs

new function() {
	CybozuLabs.MD5.calc = navigator.userAgent.match(/Firefox/) ? CybozuLabs.MD5.calc_Fx : CybozuLabs.MD5.calc_std;
};

/* globals window, exports, define */

(function(window) {
    'use strict'

    var re = {
        not_string: /[^s]/,
        not_bool: /[^t]/,
        not_type: /[^T]/,
        not_primitive: /[^v]/,
        number: /[diefg]/,
        numeric_arg: /bcdiefguxX/,
        json: /[j]/,
        not_json: /[^j]/,
        text: /^[^\x25]+/,
        modulo: /^\x25{2}/,
        placeholder: /^\x25(?:([1-9]\d*)\$|\(([^\)]+)\))?(\+)?(0|'[^$])?(-)?(\d+)?(?:\.(\d+))?([b-gijostTuvxX])/,
        key: /^([a-z_][a-z_\d]*)/i,
        key_access: /^\.([a-z_][a-z_\d]*)/i,
        index_access: /^\[(\d+)\]/,
        sign: /^[\+\-]/
    }

    function sprintf() {
        var key = arguments[0], cache = sprintf.cache
        if (!(cache[key] && cache.hasOwnProperty(key))) {
            cache[key] = sprintf.parse(key)
        }
        return sprintf.format.call(null, cache[key], arguments)
    }

    sprintf.format = function(parse_tree, argv) {
        var cursor = 1, tree_length = parse_tree.length, node_type = '', arg, output = [], i, k, match, pad, pad_character, pad_length, is_positive = true, sign = ''
        for (i = 0; i < tree_length; i++) {
            node_type = get_type(parse_tree[i])
            if (node_type === 'string') {
                output[output.length] = parse_tree[i]
            }
            else if (node_type === 'array') {
                match = parse_tree[i] // convenience purposes only
                if (match[2]) { // keyword argument
                    arg = argv[cursor]
                    for (k = 0; k < match[2].length; k++) {
                        if (!arg.hasOwnProperty(match[2][k])) {
                            throw new Error(sprintf('[sprintf] property "%s" does not exist', match[2][k]))
                        }
                        arg = arg[match[2][k]]
                    }
                }
                else if (match[1]) { // positional argument (explicit)
                    arg = argv[match[1]]
                }
                else { // positional argument (implicit)
                    arg = argv[cursor++]
                }

                if (re.not_type.test(match[8]) && re.not_primitive.test(match[8]) && get_type(arg) == 'function') {
                    arg = arg()
                }

                if (re.numeric_arg.test(match[8]) && (get_type(arg) != 'number' && isNaN(arg))) {
                    throw new TypeError(sprintf("[sprintf] expecting number but found %s", get_type(arg)))
                }

                if (re.number.test(match[8])) {
                    is_positive = arg >= 0
                }

                switch (match[8]) {
                    case 'b':
                        arg = parseInt(arg, 10).toString(2)
                    break
                    case 'c':
                        arg = String.fromCharCode(parseInt(arg, 10))
                    break
                    case 'd':
                    case 'i':
                        arg = parseInt(arg, 10)
                    break
                    case 'j':
                        arg = JSON.stringify(arg, null, match[6] ? parseInt(match[6]) : 0)
                    break
                    case 'e':
                        arg = match[7] ? parseFloat(arg).toExponential(match[7]) : parseFloat(arg).toExponential()
                    break
                    case 'f':
                        arg = match[7] ? parseFloat(arg).toFixed(match[7]) : parseFloat(arg)
                    break
                    case 'g':
                        arg = match[7] ? parseFloat(arg).toPrecision(match[7]) : parseFloat(arg)
                    break
                    case 'o':
                        arg = arg.toString(8)
                    break
                    case 's':
                        arg = String(arg)
                        arg = (match[7] ? arg.substring(0, match[7]) : arg)
                    break
                    case 't':
                        arg = String(!!arg)
                        arg = (match[7] ? arg.substring(0, match[7]) : arg)
                    break
                    case 'T':
                        arg = get_type(arg)
                        arg = (match[7] ? arg.substring(0, match[7]) : arg)
                    break
                    case 'u':
                        arg = parseInt(arg, 10) >>> 0
                    break
                    case 'v':
                        arg = arg.valueOf()
                        arg = (match[7] ? arg.substring(0, match[7]) : arg)
                    break
                    case 'x':
                        arg = parseInt(arg, 10).toString(16)
                    break
                    case 'X':
                        arg = parseInt(arg, 10).toString(16).toUpperCase()
                    break
                }
                if (re.json.test(match[8])) {
                    output[output.length] = arg
                }
                else {
                    if (re.number.test(match[8]) && (!is_positive || match[3])) {
                        sign = is_positive ? '+' : '-'
                        arg = arg.toString().replace(re.sign, '')
                    }
                    else {
                        sign = ''
                    }
                    pad_character = match[4] ? match[4] === '0' ? '0' : match[4].charAt(1) : ' '
                    pad_length = match[6] - (sign + arg).length
                    pad = match[6] ? (pad_length > 0 ? str_repeat(pad_character, pad_length) : '') : ''
                    output[output.length] = match[5] ? sign + arg + pad : (pad_character === '0' ? sign + pad + arg : pad + sign + arg)
                }
            }
        }
        return output.join('')
    }

    sprintf.cache = {}

    sprintf.parse = function(fmt) {
        var _fmt = fmt, match = [], parse_tree = [], arg_names = 0
        while (_fmt) {
            if ((match = re.text.exec(_fmt)) !== null) {
                parse_tree[parse_tree.length] = match[0]
            }
            else if ((match = re.modulo.exec(_fmt)) !== null) {
                parse_tree[parse_tree.length] = '%'
            }
            else if ((match = re.placeholder.exec(_fmt)) !== null) {
                if (match[2]) {
                    arg_names |= 1
                    var field_list = [], replacement_field = match[2], field_match = []
                    if ((field_match = re.key.exec(replacement_field)) !== null) {
                        field_list[field_list.length] = field_match[1]
                        while ((replacement_field = replacement_field.substring(field_match[0].length)) !== '') {
                            if ((field_match = re.key_access.exec(replacement_field)) !== null) {
                                field_list[field_list.length] = field_match[1]
                            }
                            else if ((field_match = re.index_access.exec(replacement_field)) !== null) {
                                field_list[field_list.length] = field_match[1]
                            }
                            else {
                                throw new SyntaxError("[sprintf] failed to parse named argument key")
                            }
                        }
                    }
                    else {
                        throw new SyntaxError("[sprintf] failed to parse named argument key")
                    }
                    match[2] = field_list
                }
                else {
                    arg_names |= 2
                }
                if (arg_names === 3) {
                    throw new Error("[sprintf] mixing positional and named placeholders is not (yet) supported")
                }
                parse_tree[parse_tree.length] = match
            }
            else {
                throw new SyntaxError("[sprintf] unexpected placeholder")
            }
            _fmt = _fmt.substring(match[0].length)
        }
        return parse_tree
    }

    var vsprintf = function(fmt, argv, _argv) {
        _argv = (argv || []).slice(0)
        _argv.splice(0, 0, fmt)
        return sprintf.apply(null, _argv)
    }

    /**
     * helpers
     */
    function get_type(variable) {
        if (typeof variable === 'number') {
            return 'number'
        }
        else if (typeof variable === 'string') {
            return 'string'
        }
        else {
            return Object.prototype.toString.call(variable).slice(8, -1).toLowerCase()
        }
    }

    var preformattedPadding = {
        '0': ['', '0', '00', '000', '0000', '00000', '000000', '0000000'],
        ' ': ['', ' ', '  ', '   ', '    ', '     ', '      ', '       '],
        '_': ['', '_', '__', '___', '____', '_____', '______', '_______'],
    }
    function str_repeat(input, multiplier) {
        if (multiplier >= 0 && multiplier <= 7 && preformattedPadding[input]) {
            return preformattedPadding[input][multiplier]
        }
        return Array(multiplier + 1).join(input)
    }

    /**
     * export to either browser or node.js
     */
    if (typeof exports !== 'undefined') {
	if (typeof module !== "undefined" && module.exports){
	    // Node.js
	    exports = module.exports = sprintf
	    exports = module.exports = vsprintf
	}else{
	    // Common.js
            exports.sprintf = sprintf
            exports.vsprintf = vsprintf
	}
    } else {
	// DOM
        window.sprintf = sprintf
        window.vsprintf = vsprintf

        if (typeof define === 'function' && define.amd) {
            define(function() {
                return {
                    sprintf: sprintf,
                    vsprintf: vsprintf
                }
            })
        }
    }
})(typeof window === 'undefined' ? this : window);


(function(window) {
    'use strict'
    /*
     * $Id$
     *
     *  IPATデータモデル操作(java script版)
     *
     *  2016.9.6 Y.Shimizu
     *  require
     *     sprintf.js
     *
     * 投票データ定義
     *   a1-5-11_b8_c1_1-2-3_4-5-6_7-8-9_1
     *   '_'がパートのデリミタ
     *       part1  a1-5-11  "a"-"曜日コード"-"競馬場コード"-"レース番号"
     *       part2  b8       "b"式別 "1":単勝 "2":複勝 ... "8":３連単
     *       part3  c1       "c"方式 self.houshiki
     *       part4  1-2-3    組番1 注) 方式により使い方が異なる
     *       part5  4-5-6    組番2
     *       part6  7-8-9    組番3 (馬単、ながしの場合は、ここがマルチON,OFF)
     *       part7  3連複,3連単の場合は、ここがマルチON,OFF
     * 
     */

    function IpatDataModel()
    {
	var self = this;

	self.shikibetu = {
            '1': '単勝',
            '2': '複勝',
            '3': '枠連',
            '4': '馬連',
            '5': 'ワイド',
            '6': '馬単',
            '7': '3連複',
            '8': '3連単',
	};
	self.houshiki = {
	    // 単勝
	    '10': '通常',
	    // 複勝
	    '20': '通常',
	    // 枠連
	    '30': '通常',
	    '31': 'フォーメーション',
	    '32': 'BOX',
	    '33': 'ながし',
	    // 馬連
	    '40': '通常',
	    '41': 'フォーメーション',
	    '42': 'BOX',
	    '43': 'ながし',
            // ワイド
            '50': '通常',
            '51': 'フォーメーション',
            '52': 'BOX',
            '53': 'ながし',
            // 馬単
            '60': '通常',
            '61': 'フォーメーション',
            '62': 'BOX',
            '63': '1着ながし',
            '64': '2着ながし',
            // 3連複
            '70': '通常',
            '71': 'フォーメーション',
            '72': 'BOX',
            '73': '軸1頭ながし',
            '76': '軸2頭ながし',
            // 3連単
            '80': '通常',
            '81': 'フォーメーション',
            '82': 'BOX',
            '83': '1着ながし',
            '84': '2着ながし',
            '85': '3着ながし',
            '86': '1,2着ながし',
            '87': '1,3着ながし',
            '88': '2,3着ながし',
	};
    };

    IpatDataModel.prototype.get_shikibetu = function()
    {
	var self = this;
	return self.shikibetu;
    }
    IpatDataModel.prototype.get_houshiki = function()
    {
	var self = this;
	return self.houshiki;
    }

    /*
     * bet_id を表記に展開
     *   waku_checkは枠連の場合に必須 (複数頭の枠番を配列で渡す)
     *    ex) waku_chaku = ['4','5','6','7','8']
     *
     */
    IpatDataModel.prototype.cvt_bet = function( bet_id, bet_money, waku_check )
    {
	var self = this;
	var part = bet_id.split(/_/);
	var s = part[1].substr(1,1);
	var h = part[2].substr(1,1);
	var is_multi = false;
	var k1 = '';
	var k2 = '';
	var k3 = '';
	

	if('1' == s || '2' == s){
	    // 単勝,複勝
            k1 = part[3];
	}else if('3' == s || '4' == s || '5' == s){
	    // 枠連,馬連,ワイド
            if('0' == h || '1' == h || '3' == h){
		// 通常,フォーメーション,ながし
		k1 = part[3];
		k2 = part[4];
            }else{
		// BOX
		k1 = part[3];
            }
	}else if('6' == s){
	    // 馬単
            if('0' ==h || '1' == h || '3' == h || '4' == h){
		// 通常,フォーメーション,1着ながし,2着ながし
		k1 = part[3];
		k2 = part[4];
		if('1' == part[5]){
                    is_multi = true;
		}else{
                    is_multi = false;
		}
            }else{
		// BOX
		k1 = part[3];
            }
	}else if('7' == s){
	    // ３連複
            if('0' == h || '1' == h){
		k1 = part[3];
		k2 = part[4];
		k3 = part[5];
            }else if('2' == h){
		k1 = part[3];
            }else if('3' == h){
		k1 = part[3];
		k2 = part[4];
            }else if('6' == h){
		k1 = part[3];
		k2 = part[4];
		k3 = part[5];
            }
	}else if('8' == s){
	    // ３連単
            if('0' == h || '1' == h){
		k1 = part[3];
		k2 = part[4];
		k3 = part[5];

            }else if('2' == h){
		k1 = part[3];
            }else if('3' == h || '4' == h || '5' == h){
		k1 = part[3];
		k2 = part[4];
		if('1' == part[5]){
                    is_multi = true;
		}else{
                    is_multi = false;
		}
            }else if('6' == h || '7' == h || '8' == h){
		k1 = part[3];
		k2 = part[4];
		k3 = part[5];
		if('1' == part[6]){
                    is_multi = true;
		}else{
                    is_multi = false;
		}
            }
	}
	//	console.log('s:%s h:%s k1:%s k2:%s k3:%s m:%b',s,h,k1,k2,k3,is_multi);
	var bet = {
            bet_id: bet_id,
            shikibetu: s,
            shikibetu_name: self.shikibetu[s],
            houshiki: h,
            houshiki_name: '',
	    kumi_name : '',
            kaime1: k1,
            kaime2: k2,
            kaime3: k3,
            is_multi: is_multi,
            bet_money: bet_money,
            bet_money_total: 0,
            bet_count: 0,
            comb: null,
	};

	if('0' != h){
            bet.comb = self.make_combination(bet_id, waku_check);
	    bet.bet_count = bet.comb.length;
	    bet.bet_money_total = bet_money * bet.bet_count;
	}else{
	    bet.bet_count = 1;
	    bet.bet_money_total = bet_money;
	}
	var info = self.bet_name( bet );
	bet.houshiki_name = info['houshiki_name'];
	bet.kumi_name = info['kumi_name'];
	
	return bet;
    }

    /*
     * 方式名、買い目要約を配列で返す
     */
    IpatDataModel.prototype.bet_name = function( bet )
    {
	var self = this;
	var bet_info = {};
	var kumi = '';
	bet_info['houshiki_name'] = self.houshiki[bet.shikibetu + bet.houshiki];

	if('0' == bet.houshiki){

	}else{
            if('3' == bet.shikibetu
               || '4' == bet.shikibetu
               || '5' == bet.shikibetu
               || '6' == bet.shikibetu){ 
		// 枠連,馬連,ワイド,馬単
		if('1' == bet.houshiki
		   || '2' == bet.houshiki){
                    kumi = sprintf("%s組",bet.comb.length);
		}else if('3' == bet.houshiki){
                    if(bet.is_multi){
			kumi = sprintf("%02s-**", parseInt(bet.kaime1));
                    }else{
			var val = bet.kaime2.split(/-/);
			kumi = sprintf("%s@@%d頭",bet.kaime1,parseInt(val.length));
                    }
		}else if('4' == bet.houshiki){
                    if(bet.is_multi){
			kumi = sprintf("**-%02s",bet.kaime1);
                    }else{
			var val = bet.kaime2.split(/-/);
			kumi = sprintf("%d頭@@%s",parseInt(val.length),bet.kaime1);
                    }
		}
            }else if('7' == bet.shikibetu){
		if('1' == bet.houshiki
		   || '2' == bet.houshiki){
                    kumi = sprintf("%d組",parseInt(bet.comb.length));
		}else if('3' == bet.houshiki){
                    kumi = sprintf("%02s-**-**",bet.kaime1);
		}else if('6' == bet.houshiki){
                    kumi = sprintf("%02d-%02d-**",parseInt(bet.kaime1),parseInt(bet.kaime2));
		}
            }else if('8' == bet.shikibetu){
		if('1' == bet.houshiki
		   || '2' == bet.houshiki){
                    kumi = sprintf("%d組", parseInt(bet.comb.length));
		}else if('3' == bet.houshiki || '4' == bet.houshiki || '5' == bet.houshiki){
                    var val2 = bet.kaime2.split(/-/);
                    kumi = sprintf("%02d@@%d頭", parseInt(bet.kaime1), parseInt(val2.length));
		}else if('6' == bet.houshiki || '7' == bet.houshiki || '8' == bet.houshiki){
                    if(bet.is_multi){
			kumi = sprintf("%02s@@%02d*****",bet.kaime1, parseInt(bet.kaime2));
                    }else{
			var val3 = bet.kaime3.split(/-/);
			kumi = sprintf("%02s@@%02d@@%d頭",bet.kaime1, parseInt(bet.kaime2), parseInt(val3.length));
                    }
		}
            }
	}
	bet_info['kumi_name'] = kumi.replace(/@@/g,'→');
	return bet_info;
    }

    //----- private -------------------------------------------------------

    /*
     * public
     * 通常投票以外(まとめ買い)の組み合わせを展開する
     */
    IpatDataModel.prototype.make_combination = function( kaime, waku_check )
    {
	var self = this;
	var part = kaime.split(/_/);
	var s = part[1].substr(1,1);
	var h = part[2].substr(1,1);
	var p1 = part[3] && part[3].split(/-/);
	var p2 = part[4] && part[4].split(/-/);
	var p3 = part[5] && part[5].split(/-/);
	var multi = false;
	//    console.log('part:', part);

	var comb;
	if('0' == h){
            return false;
	}
	if('1' == s || '2' == s){
            // 単勝,複勝
            return false;
	}else if('3' == s){
            // 枠連
            comb = self.gen_wakuren(h, p1, p2, waku_check);
	}else if('4' == s){
            // 馬連
            comb = self.gen_umaren(h, p1, p2);
	}else if('5' == s){
            // ワイド
            comb = self.gen_wide(h, p1, p2);
	}else if('6' == s){
            // 馬単
            comb = self.gen_umatan(h, p1, p2 ,p3);
	}else if('7' == s){
            // 3連複
            comb = self.gen_renfuku3(h, p1, p2, p3);
	}else if('8' == s){
	    if('3' == h || '4' == h || '5' == h){
		multi = part[5];
	    }else if('6' == h || '7' == h || '8' == h){
		multi = part[6];
	    }
	    // 3連単
            comb = self.gen_rentan3(h, p1, p2, p3, multi);
	}
	return comb;
    }

    /*
     * public
     * 枠連の買い目を展開する
     * h: 方式  self.houshikiの2バイト目 
     * p1: 枠番の配列(軸)
     * p2: 枠番の配列(相手)
     *   BOXの場合p1のみ
     */
    IpatDataModel.prototype.gen_wakuren = function( h, p1, p2, waku_check )
    {
	var self = this;
	var tmp = [];
	if('1' == h || '3' ==h){      // フォーメーション or  1着(軸1頭)流し
	    tmp = self._combine(p1, p2);
	}else if('2' == h){	// BOX
	    tmp = self._combine(p1, p1);
	}
	var ah = {};
	for(var i = 0; i < tmp.length; i++){
	    if( parseInt(tmp[i][0]) == parseInt(tmp[i][1]) ){
		if('1' == h || '3' == h){	// '1':フォーメーション or '3':流し 
		    // ２つの枠番が共に複数頭枠か？
		    if(self._in_array(tmp[i][0], waku_check) && self._in_array(tmp[i][1], waku_check)){
			ah[ sprintf("%02d-%02d", parseInt(tmp[i][0]), parseInt(tmp[i][1])) ] = true;
		    }
		}
	    }else if( parseInt(tmp[i][0]) > parseInt(tmp[i][1]) ){
		ah[ sprintf("%02d-%02d", parseInt(tmp[i][1]), parseInt(tmp[i][0])) ] = true;
	    }else{
		ah[ sprintf("%02d-%02d", parseInt(tmp[i][0]), parseInt(tmp[i][1])) ] = true;
	    }
	}
	return Object.keys(ah);
    }

    /*
     * public
     * 馬連の買い目を展開する
     * h: 方式  self.houshikiの2バイト目 
     * p1: 馬番の配列(軸)
     * p2: 馬番の配列(相手)
     *   BOXの場合p1のみ
     */
    IpatDataModel.prototype.gen_umaren = function( h, p1, p2 )
    {
	var self = this;
	
	var tmp = [];
	if('1' == h || '3' ==h){      // フォーメーション or  1着(軸1頭)流し
	    tmp = self._combine(p1, p2);
	}else if('2' == h){	// BOX
	    tmp = self._combine(p1, p1);
	}
	var ah = [];
	for(var i = 0; i < tmp.length; i++){
	    var a = '';
	    var b = '';
	    if( parseInt(tmp[i][0]) == parseInt(tmp[i][1]) ){
		continue;
	    }else if( parseInt(tmp[i][0]) > parseInt(tmp[i][1]) ){
		ah[ sprintf("%02d-%02d", parseInt(tmp[i][1]), parseInt(tmp[i][0])) ] = true;
	    }else{
		ah[ sprintf("%02d-%02d", parseInt(tmp[i][0]), parseInt(tmp[i][1])) ] = true;
	    }
	}
	return Object.keys(ah);
    }

    /*
     * public
     * ワイドの買い目を展開
     */
    IpatDataModel.prototype.gen_wide = function( h, p1, p2 )
    {
	var self = this;
	return self.gen_umaren(h ,p1 ,p2);
    }

    /*
     * public
     * 馬単の買い目を展開
     * h: 方式  self.houshikiの2バイト目 
     * p1: 馬番の配列(軸)
     * p2: 馬番の配列(相手)
     *   BOXの場合p1のみ
     *   2着ながしは、p2が軸
     */
    IpatDataModel.prototype.gen_umatan = function( h, p1, p2, multi )
    {
	var self = this;
	var tmp = [];
	if('1' == h || '3' == h){      // フォーメーション or 1着(軸1頭)流し
	    tmp = self._combine(p1, p2);
	}else if('2' == h){	// BOX
	    tmp = self._combine(p1, p1);
	}else if('4' == h){	// 2着(軸1頭)流し
	    tmp = self._combine(p2, p1);
	}else{
	    return false;
	}
	var ar = [];
	for(var i = 0; i < tmp.length; i++){
	    if( parseInt(tmp[i][0]) == parseInt(tmp[i][1]) ){
		continue;
	    }else{
		ar.push( sprintf("%02d-%02d", parseInt(tmp[i][0]), parseInt(tmp[i][1])) );
		if(undefined != multi && true == multi){
		    ar.push( sprintf("%02d-%02d", parseInt(tmp[i][1]), parseInt(tmp[i][0])) );
		}
	    }
	}
	ar.sort(function(a,b){
	    if( a < b ) return -1;
	    if( a > b ) return 1;
	    return 0;
	});
	return ar;
    }

    /*
     * public
     * 3連複の買い目を展開
     * h: 方式  self.houshikiの2バイト目 
     * p1: 馬番の配列1
     * p2: 馬番の配列2
     * p3: 馬番の配列3
     *   BOXの場合p1のみ
     */
    IpatDataModel.prototype.gen_renfuku3 = function( h, p1, p2, p3 )
    {
	var self = this;
	var tmp;
	if('1' == h){// フォーメーション
	    tmp = self._combine(p1, p2, p3);
	}else if('2' == h){	// BOX
	    tmp = self._combine(p1, p1, p1);
	}else if('3' == h){     // 軸1頭流し
	    tmp = self._combine(p1, p2, p2);
	}else if('6' == h){	// 軸2頭流し
	    tmp = self._combine(p1, p2, p3);
	}else{
	    return false;
	}
	var ah = {};
	for(var i = 0; i < tmp.length; i++){
	    ah[ sprintf("%02d-%02d-%02d",parseInt(tmp[i][0]),parseInt(tmp[i][1]),parseInt(tmp[i][2])) ] = true;
	    ah[ sprintf("%02d-%02d-%02d",parseInt(tmp[i][0]),parseInt(tmp[i][2]),parseInt(tmp[i][1])) ] = true;
	    ah[ sprintf("%02d-%02d-%02d",parseInt(tmp[i][1]),parseInt(tmp[i][0]),parseInt(tmp[i][2])) ] = true;
	    ah[ sprintf("%02d-%02d-%02d",parseInt(tmp[i][1]),parseInt(tmp[i][2]),parseInt(tmp[i][0])) ] = true;
	    ah[ sprintf("%02d-%02d-%02d",parseInt(tmp[i][2]),parseInt(tmp[i][0]),parseInt(tmp[i][1])) ] = true;
	    ah[ sprintf("%02d-%02d-%02d",parseInt(tmp[i][2]),parseInt(tmp[i][1]),parseInt(tmp[i][0])) ] = true;
	}
	var ar = [];
	for(var r in ah){
	    var k = r.split(/-/);
            if(k[0] == k[1] || k[0] == k[2] || k[1] == k[2]){	// exclude
            }else if(k[0] > k[1] || k[0] > k[2] || k[1] > k[2]){	// exclude
            }else{
		ar.push( r );
            }
	}
	ar.sort(function(a,b){
	    if( a < b ) return -1;
	    if( a > b ) return 1;
	    return 0;
	});
	return ar;
    }

    /*
     * public
     * 3連単の買い目を展開
     * h: 方式  self.houshikiの2バイト目 
     * p1: 馬番の配列1
     * p2: 馬番の配列2
     * p3: 馬番の配列3
     * multi: マルチ true:あり
     *   BOXの場合p1のみ
     */
    IpatDataModel.prototype.gen_rentan3 = function( h, p1, p2, p3, multi )
    {
	var self = this;
	var tmp;
	if('1' == h){      // フォーメーション
	    tmp = self._combine(p1, p2, p3);
	}else if('2' == h){	// BOX
	    tmp = self._combine(p1, p1, p1);
	}else if('3' == h){	// 1着(軸1頭)流し
	    tmp = self._combine(p1, p2, p2);
	}else if('4' == h){	// 2着(軸1頭)流し
	    tmp = self._combine(p2, p1, p2);
	}else if('5' == h){	// 3着(軸1頭)流し
	    tmp = self._combine(p2, p2, p1);
	}else if('6' == h){	// 1,2着(軸2頭)流し
	    tmp = self._combine(p1, p2, p3);
	}else if('7' == h){	// 1,3着(軸2頭)流し
	    tmp = self._combine(p1, p3, p2);
	}else if('8' == h){	// 2,3着(軸2頭)流し
	    tmp = self._combine(p3, p1, p2);
	}else{
	    return false;
	}

	var ah = {};
	for(var i = 0; i < tmp.length; i++){
	    ah[ sprintf("%02d-%02d-%02d", parseInt(tmp[i][0]), parseInt(tmp[i][1]), parseInt(tmp[i][2])) ] = true;
	    if(multi){
		ah[ sprintf("%02d-%02d-%02d", parseInt(tmp[i][0]), parseInt(tmp[i][2]), parseInt(tmp[i][1])) ] = true;
		ah[ sprintf("%02d-%02d-%02d", parseInt(tmp[i][1]), parseInt(tmp[i][0]), parseInt(tmp[i][2])) ] = true;
		ah[ sprintf("%02d-%02d-%02d", parseInt(tmp[i][1]), parseInt(tmp[i][2]), parseInt(tmp[i][0])) ] = true;
		ah[ sprintf("%02d-%02d-%02d", parseInt(tmp[i][2]), parseInt(tmp[i][0]), parseInt(tmp[i][1])) ] = true;
		ah[ sprintf("%02d-%02d-%02d", parseInt(tmp[i][2]), parseInt(tmp[i][1]), parseInt(tmp[i][0])) ] = true;
	    }
	}
	
	var ar = [];
	for(var r in ah){
	    var k = r.split(/-/);
            if(k[0] == k[1] || k[0] == k[2] || k[1] == k[2]){	// exclude
		//        }else if(k[0] > k[1] || k[0] > k[2] || k[1] > k[2]){	// exclude
            }else{
		ar.push( r );
            }
	}
	ar.sort(function(a,b){
	    if( a < b ) return -1;
	    if( a > b ) return 1;
	    return 0;
	});
	return ar;
    }

    /*
     * private
     * 番号配列よりの組み合わせを生成(3つまで限定)
     */
    IpatDataModel.prototype._combine = function()
    {
	var self = this;
	var argv = arguments;

	var argc = argv.length;
	//    console.log('argc: %d argv: %O',argc,argv);
	if(argc < 2) return false;

	var new_a = [];
	var p1 = argv[0];
	var p2 = argv[1];
	var p3 = argv[2] || [];
	
	if(2 == argc){
	    for(var i=0; i < p1.length; i++){
		for(var j=0; j < p2.length; j++){
		    new_a.push( [p1[i], p2[j]] );
		}
	    }
	}else if(3 == argc){
	    for(var i=0; i < p1.length; i++){
		for(var j=0; j < p2.length; j++){
		    for(var k=0; k < p3.length; k++){
			new_a.push( [p1[i], p2[j], p3[k]] );
		    }
		}
	    }
	}
	return new_a;
    }
    IpatDataModel.prototype._in_array = function (val, arr)
    {
	if(undefined === arr){
	    return false;
	}
	return (-1 !== arr.indexOf(val)) ? true : false;
    }

    /**
     * export to either browser or node.js
     */
    if (typeof exports !== 'undefined') {
	if (typeof module !== "undefined" && module.exports){
	    // Node.js
	    exports = module.exports = IpatDataModel
//	    var sprintf = require('sprintf');
	}else{
	    // Common.js
	    exports.IpatDataModel = IpatDataModel
	}
    } else {
	// DOM
        window.IpatDataModel = IpatDataModel

        if (typeof define === 'function' && define.amd) {
            define(function() {
                return {
                    IpatDataModel: IpatDataModel
                }
            })
        }
    }
    
})(typeof window === 'undefined' ? this : window);



(function(window) {
    'use strict'
    /*
     * $Id$
     *
     *  IPAT投票フォームジェネレータ(中央版)
     *
     *  2016.9.11 Y.Shimizu
     *  require
     *     IpatDataModel.js sprintf.js
     * 
     */

    function IpatMarkSheetJRA()
    {
	var self = this;
    };

    /*
     * 買い目をIPAT POSTデータフォーマットに変換
     *   ary_kaime = [
     *        {bet_id: 'a7-6-11_b8_c0_3_5_4', bet_money: 100},
     *   ];
     *     bet_id: 買い目コード, bet_money: 投票金額の配列 (複数可)
     *   waku_check = ['6','7','8'];
     *     買い目に枠連が含まれる場合のみ。複数頭枠の枠番を配列で示す。
     */
    IpatMarkSheetJRA.prototype.cvt_sheet = function( ary_kaime, waku_check )
    {
	var self = this;
	var seq = 0;
	var ary_sheet = [];
	for(var idx=0; idx < ary_kaime.length; idx++){
	    var row = ary_kaime[idx];
            var part = row.bet_id.split(/_/);
	    //	console.log('part:', part);
            var val = part[0].split(/-/);
            var youbi_cd = val[0].substr(1,1);
            var jyo_cd = sprintf("%X", parseInt(val[1]));
            var race_no = sprintf("%X", parseInt(val[2]));
            var shikibetu = part[1].substr(1,1);
            var houshiki = part[2].substr(1,1);
	    //console.log("shikibetu: %s houshiki: %s",shikibetu,houshiki);
	    var is_multi;
	    
            var mark;
	    mark = '';
            mark += sprintf("1%03d",seq);
            mark += jyo_cd;
            mark += race_no;
            mark += youbi_cd;
            mark += houshiki;
            mark += shikibetu;

            // 組番
            if('1' == shikibetu || '2' == shikibetu){
		// 単勝,複勝
		mark += self._cvt_kumi(part[3],'0','0',false);
            }else if('3' == shikibetu){
		// 枠連
		if('0' == houshiki){
                    mark += self._cvt_kumi(part[3],part[4],'0',false);
		}else if('1' == houshiki){ // フォーメーション
                    // 組合せで複数枠番(ゾロ目)の買い目がある分、組番３のシートに設定
		    ipat_d = new IpatDataModel();
                    var ary_ret = ipat_d.make_combination(row.kaime, ary_waku_check);
                    var waku3;
                    for(var kaime in ary_ret){
			kumi = explode('-',kaime);
			if(kumi[0] == kumi[1]){
                            waku3.push( kumi[0] );
			}
                    }
                    waku3_str = '';
                    if(count(waku3) > 0){
			waku3_str += implode('-',waku3);
			mark += self._cvt_kumi(part[3],part[4],waku3_str,false);
                    }else{
			mark += self._cvt_kumi(part[3],part[4],'0',false);
                    }
		}else if('2' == houshiki){ // BOX
                    mark += self._cvt_kumi(part[3],'0','0',false);
		}else if('3' == houshiki){ // 流し(1着,軸1頭)
                    // 流しは、組番1と組番3のシートに設定
                    mark += self._cvt_kumi(part[3],'0',part[4],false);
		}
            }else if('4' == shikibetu || '5' == shikibetu || '6' == shikibetu){
		// 馬連,ワイド,馬単
		if('0' == houshiki){
                    mark += self._cvt_kumi(part[3],part[4],'0',false);
		}else if('1' == houshiki){ // フォーメーション
                    mark += self._cvt_kumi(part[3],part[4],'0',false);
		}else if('2' == houshiki){ // BOX
                    mark += self._cvt_kumi(part[3],'0','0',false);
		}else if('3' == houshiki){ // 流し(1着,軸1頭)
                    // 流しは、組番1と組番3のシートに設定
                    if('1' == part[5]){
			is_multi = true;
                    }else{
			is_multi = false;
                    }
                    mark += self._cvt_kumi(part[3],'0',part[4],is_multi);
		}else if('4' == houshiki){ // 流し(2着)
                    if('1' == part[5]){
			is_multi = true;
                    }else{
			is_multi = false;
                    }
                    // 2連式流しは、組番1と組番3のシートに設定
                    mark += self._cvt_kumi(part[3],'0',part[4],is_multi);
		}
            }else if('7' == shikibetu || '8' == shikibetu){
		// 3連複,3連単
		if('0' == houshiki){
                    mark += self._cvt_kumi(part[3],part[4],part[5],false);
		}else if('1' == houshiki){ // フォーメーション
                    mark += self._cvt_kumi(part[3],part[4],part[5],false);
		}else if('2' == houshiki){ // BOX
                    mark += self._cvt_kumi(part[3],'0','0',false);
		}else if('3' == houshiki || '4' == houshiki || '5' == houshiki){
                    // 1着流し,2着流し,3着流し,
                    // 流しは、組番1と組番3のシートに設定
                    if('1' == part[5]){
			is_multi = true;
                    }else{
			is_multi = false;
                    }
                    mark += self._cvt_kumi(part[3],'0',part[4],is_multi);
		}else if('6' == houshiki || '7' == houshiki || '8' == houshiki){ 
                    if('1' == part[6]){
			is_multi = true;
                    }else{
			is_multi = false;
                    }
                    mark += self._cvt_kumi(part[3],part[4],part[5],is_multi);
		}
            }
            // 金額
            mark += self._cvt_money( row.bet_money );
            seq++;
            ary_sheet.push( mark );
            //console.log("mark: %s",mark);
	}
	return ary_sheet;
    }

    /*
     * private
     * 入力金額をIPATマークシート形式にする
     */
    IpatMarkSheetJRA.prototype._cvt_money = function( bet_money )
    {
	var self = this;
	var str = self._bin2hex( self._pack('n', parseInt(bet_money / 100)) );  // ビッグエンディアン
	//    console.log('bet_money: %s str: %s',bet_money,str);
	// strtoupper();
	return str;
    }

    /*
     * private
     * 投票内容の組番部分
     */
    IpatMarkSheetJRA.prototype._cvt_kumi = function( k1, k2, k3, is_multi )
    {
	var self = this;
	//    console.log('_cvt_kumi', k1, k2, k3, is_multi);
	var src = [k1, k2, k3];
	var sheet = [];

	for(var i=0 ; i < src.length; i++){
            var row = {};
            for(var j=1; j <= 18; j++){
		row[j] = false;
	    }

	    var kumi = src[i].split(/-/);
	    //	console.log('kumi.length: %s',kumi.length);
            for(var k=0; k < kumi.length; k++){
		if(undefined != row[ kumi[k] ]){
		    row[ kumi[k] ] = true;
		}
	    }
            sheet.push( row ); 
	}
	//    console.log(sheet);

	var char_map = '';
	for(i=0; i < sheet.length; i++){
	    var tmp = [];
	    for(var no in sheet[i]){
		if(true == sheet[i][no]){
		    char_map += '1';
		}else{
		    char_map += '0';
		}
	    }
	}

	if(true == is_multi){
            char_map += '01';
	}else{
            char_map += '00';
	}
	//    console.log("size: %d char_map: %s",char_map.length,char_map);

	var ret = '';
	for(i = 0; i < 7; i++){
	    var bin_str = char_map.substr( i * 8, 8 );
	    bin_str = (bin_str + '').replace(/[^01]/gi, '');	// bindec(php)
	    var dec = parseInt(bin_str, 2);			// bindec(php)
            ret += sprintf("%02x",dec);
	}
	return ret;
    }

    IpatMarkSheetJRA.prototype._pack = function( format )
    {
	var self = this;
	//  discuss at: http://locutus.io/php/pack/
	// original by: Tim de Koning (http://www.kingsquare.nl)
	//    parts by: Jonas Raoni Soares Silva (http://www.jsfromhell.com)
	// bugfixed by: Tim de Koning (http://www.kingsquare.nl)
	//      note 1: Float encoding by: Jonas Raoni Soares Silva
	//      note 1: Home: http://www.kingsquare.nl/blog/12-12-2009/13507444
	//      note 1: Feedback: phpjs-pack@kingsquare.nl
	//      note 1: "machine dependent byte order and size" aren't
	//      note 1: applicable for JavaScript; pack works as on a 32bit,
	//      note 1: little endian machine.
	//   example 1: pack('nvc*', 0x1234, 0x5678, 65, 66)
	//   returns 1: '\u00124xVAB'
	//   example 2: pack('H4', '2345')
	//   returns 2: '#E'
	//   example 3: pack('H*', 'D5')
	//   returns 3: 'O'
	//   example 4: pack('d', -100.876)
	//   returns 4: "\u0000\u0000\u0000\u0000\u00008YA"
	//        test: skip-1

	var formatPointer = 0
	var argumentPointer = 1
	var result = ''
	var argument = ''
	var i = 0
	var r = []
	var instruction, quantifier, word, precisionBits, exponentBits, extraNullCount

	// vars used by float encoding
	var bias
	var minExp
	var maxExp
	var minUnnormExp
	var status
	var exp
	var len
	var bin
	var signal
	var n
	var intPart
	var floatPart
	var lastBit
	var rounded
	var j
	var k
	var tmpResult

	while (formatPointer < format.length) {
	    instruction = format.charAt(formatPointer)
	    quantifier = ''
	    formatPointer++
	    while ((formatPointer < format.length) && (format.charAt(formatPointer)
						       .match(/[\d\*]/) !== null)) {
		quantifier += format.charAt(formatPointer)
		formatPointer++
	    }
	    if (quantifier === '') {
		quantifier = '1'
	    }

	    // Now pack variables: 'quantifier' times 'instruction'
	    switch (instruction) {
	    case 'a':
	    case 'A':
		// NUL-padded string
		// SPACE-padded string
		if (typeof arguments[argumentPointer] === 'undefined') {
		    //		throw new Error('Warning:  pack() Type ' + instruction + ': not enough arguments')
		} else {
		    argument = String(arguments[argumentPointer])
		}
		if (quantifier === '*') {
		    quantifier = argument.length
		}
		for (i = 0; i < quantifier; i++) {
		    if (typeof argument[i] === 'undefined') {
			if (instruction === 'a') {
			    result += String.fromCharCode(0)
			} else {
			    result += ' '
			}
		    } else {
			result += argument[i]
		    }
		}
		argumentPointer++
		break
	    case 'h':
	    case 'H':
		// Hex string, low nibble first
		// Hex string, high nibble first
		if (typeof arguments[argumentPointer] === 'undefined') {
		    //		throw new Error('Warning: pack() Type ' + instruction + ': not enough arguments')
		} else {
		    argument = arguments[argumentPointer]
		}
		if (quantifier === '*') {
		    quantifier = argument.length
		}
		if (quantifier > argument.length) {
		    var msg = 'Warning: pack() Type ' + instruction + ': not enough characters in string'
		    //		throw new Error(msg)
		}

		for (i = 0; i < quantifier; i += 2) {
		    // Always get per 2 bytes...
		    word = argument[i]
		    if (((i + 1) >= quantifier) || typeof argument[i + 1] === 'undefined') {
			word += '0'
		    } else {
			word += argument[i + 1]
		    }
		    // The fastest way to reverse?
		    if (instruction === 'h') {
			word = word[1] + word[0]
		    }
		    result += String.fromCharCode(parseInt(word, 16))
		}
		argumentPointer++
		break

	    case 'c':
	    case 'C':
		// signed char
		// unsigned char
		// c and C is the same in pack
		if (quantifier === '*') {
		    quantifier = arguments.length - argumentPointer
		}
		if (quantifier > (arguments.length - argumentPointer)) {
		    //		throw new Error('Warning:  pack() Type ' + instruction + ': too few arguments')
		}

		for (i = 0; i < quantifier; i++) {
		    result += String.fromCharCode(arguments[argumentPointer])
		    argumentPointer++
		}
		break

	    case 's':
	    case 'S':
	    case 'v':
		// signed short (always 16 bit, machine byte order)
		// unsigned short (always 16 bit, machine byte order)
		// s and S is the same in pack
		if (quantifier === '*') {
		    quantifier = arguments.length - argumentPointer
		}
		if (quantifier > (arguments.length - argumentPointer)) {
		    //		throw new Error('Warning:  pack() Type ' + instruction + ': too few arguments')
		}

		for (i = 0; i < quantifier; i++) {
		    result += String.fromCharCode(arguments[argumentPointer] & 0xFF)
		    result += String.fromCharCode(arguments[argumentPointer] >> 8 & 0xFF)
		    argumentPointer++
		}
		break

	    case 'n':
		// unsigned short (always 16 bit, big endian byte order)
		if (quantifier === '*') {
		    quantifier = arguments.length - argumentPointer
		}
		if (quantifier > (arguments.length - argumentPointer)) {
		    //		throw new Error('Warning: pack() Type ' + instruction + ': too few arguments')
		}

		for (i = 0; i < quantifier; i++) {
		    result += String.fromCharCode(arguments[argumentPointer] >> 8 & 0xFF)
		    result += String.fromCharCode(arguments[argumentPointer] & 0xFF)
		    argumentPointer++
		}
		break

	    case 'i':
	    case 'I':
	    case 'l':
	    case 'L':
	    case 'V':
		// signed integer (machine dependent size and byte order)
		// unsigned integer (machine dependent size and byte order)
		// signed long (always 32 bit, machine byte order)
		// unsigned long (always 32 bit, machine byte order)
		// unsigned long (always 32 bit, little endian byte order)
		if (quantifier === '*') {
		    quantifier = arguments.length - argumentPointer
		}
		if (quantifier > (arguments.length - argumentPointer)) {
		    //		throw new Error('Warning:  pack() Type ' + instruction + ': too few arguments')
		}

		for (i = 0; i < quantifier; i++) {
		    result += String.fromCharCode(arguments[argumentPointer] & 0xFF)
		    result += String.fromCharCode(arguments[argumentPointer] >> 8 & 0xFF)
		    result += String.fromCharCode(arguments[argumentPointer] >> 16 & 0xFF)
		    result += String.fromCharCode(arguments[argumentPointer] >> 24 & 0xFF)
		    argumentPointer++
		}

		break
	    case 'N':
		// unsigned long (always 32 bit, big endian byte order)
		if (quantifier === '*') {
		    quantifier = arguments.length - argumentPointer
		}
		if (quantifier > (arguments.length - argumentPointer)) {
		    //		throw new Error('Warning:  pack() Type ' + instruction + ': too few arguments')
		}

		for (i = 0; i < quantifier; i++) {
		    result += String.fromCharCode(arguments[argumentPointer] >> 24 & 0xFF)
		    result += String.fromCharCode(arguments[argumentPointer] >> 16 & 0xFF)
		    result += String.fromCharCode(arguments[argumentPointer] >> 8 & 0xFF)
		    result += String.fromCharCode(arguments[argumentPointer] & 0xFF)
		    argumentPointer++
		}
		break

	    case 'f':
	    case 'd':
		// float (machine dependent size and representation)
		// double (machine dependent size and representation)
		// version based on IEEE754
		precisionBits = 23
		exponentBits = 8
		if (instruction === 'd') {
		    precisionBits = 52
		    exponentBits = 11
		}

		if (quantifier === '*') {
		    quantifier = arguments.length - argumentPointer
		}
		if (quantifier > (arguments.length - argumentPointer)) {
		    //		throw new Error('Warning:  pack() Type ' + instruction + ': too few arguments')
		}
		for (i = 0; i < quantifier; i++) {
		    argument = arguments[argumentPointer]
		    bias = Math.pow(2, exponentBits - 1) - 1
		    minExp = -bias + 1
		    maxExp = bias
		    minUnnormExp = minExp - precisionBits
		    status = isNaN(n = parseFloat(argument)) || n === -Infinity || n === +Infinity ? n : 0
		    exp = 0
		    len = 2 * bias + 1 + precisionBits + 3
		    bin = new Array(len)
		    signal = (n = status !== 0 ? 0 : n) < 0
		    n = Math.abs(n)
		    intPart = Math.floor(n)
		    floatPart = n - intPart

		    for (k = len; k;) {
			bin[--k] = 0
		    }
		    for (k = bias + 2; intPart && k;) {
			bin[--k] = intPart % 2
			intPart = Math.floor(intPart / 2)
		    }
		    for (k = bias + 1; floatPart > 0 && k; --floatPart) {
			(bin[++k] = ((floatPart *= 2) >= 1) - 0)
		    }
		    for (k = -1; ++k < len && !bin[k];) {}

		    // @todo: Make this more readable:
		    var key = (lastBit = precisionBits - 1 +
			       (k =
				(exp = bias + 1 - k) >= minExp &&
				exp <= maxExp ? k + 1 : bias + 1 - (exp = minExp - 1))) + 1

		    if (bin[key]) {
			if (!(rounded = bin[lastBit])) {
			    for (j = lastBit + 2; !rounded && j < len; rounded = bin[j++]) {}
			}
			for (j = lastBit + 1; rounded && --j >= 0;
			     (bin[j] = !bin[j] - 0) && (rounded = 0)) {}
		    }

		    for (k = k - 2 < 0 ? -1 : k - 3; ++k < len && !bin[k];) {}

		    if ((exp = bias + 1 - k) >= minExp && exp <= maxExp) {
			++k
		    } else {
			if (exp < minExp) {
			    if (exp !== bias + 1 - len && exp < minUnnormExp) {
				// "encodeFloat::float underflow"
			    }
			    k = bias + 1 - (exp = minExp - 1)
			}
		    }

		    if (intPart || status !== 0) {
			exp = maxExp + 1
			k = bias + 2
			if (status === -Infinity) {
			    signal = 1
			} else if (isNaN(status)) {
			    bin[k] = 1
			}
		    }

		    n = Math.abs(exp + bias)
		    tmpResult = ''

		    for (j = exponentBits + 1; --j;) {
			tmpResult = (n % 2) + tmpResult
			n = n >>= 1
		    }

		    n = 0
		    j = 0
		    k = (tmpResult = (signal ? '1' : '0') + tmpResult + (bin
									 .slice(k, k + precisionBits)
									 .join(''))
			).length
		    r = []

		    for (; k;) {
			n += (1 << j) * tmpResult.charAt(--k)
			if (j === 7) {
			    r[r.length] = String.fromCharCode(n)
			    n = 0
			}
			j = (j + 1) % 8
		    }

		    r[r.length] = n ? String.fromCharCode(n) : ''
		    result += r.join('')
		    argumentPointer++
		}
		break

	    case 'x':
		// NUL byte
		if (quantifier === '*') {
		    //		throw new Error('Warning: pack(): Type x: \'*\' ignored')
		}
		for (i = 0; i < quantifier; i++) {
		    result += String.fromCharCode(0)
		}
		break

	    case 'X':
		// Back up one byte
		if (quantifier === '*') {
		    //		throw new Error('Warning: pack(): Type X: \'*\' ignored')
		}
		for (i = 0; i < quantifier; i++) {
		    if (result.length === 0) {
			//		    throw new Error('Warning: pack(): Type X:' + ' outside of string')
		    } else {
			result = result.substring(0, result.length - 1)
		    }
		}
		break

	    case '@':
		// NUL-fill to absolute position
		if (quantifier === '*') {
		    //		throw new Error('Warning: pack(): Type X: \'*\' ignored')
		}
		if (quantifier > result.length) {
		    extraNullCount = quantifier - result.length
		    for (i = 0; i < extraNullCount; i++) {
			result += String.fromCharCode(0)
		    }
		}
		if (quantifier < result.length) {
		    result = result.substring(0, quantifier)
		}
		break

	    default:
		//	    throw new Error('Warning: pack() Type ' + instruction + ': unknown format code')
	    }
	}
	if (argumentPointer < arguments.length) {
	    var msg2 = 'Warning: pack(): ' + (arguments.length - argumentPointer) + ' arguments unused'
	    //	throw new Error(msg2)
	}

	return result
    }
    IpatMarkSheetJRA.prototype._bin2hex = function( s )
    {
	var self = this;
	// From: http://phpjs.org/functions
	// +   original by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
	// +   bugfixed by: Onno Marsman
	// +   bugfixed by: Linuxworld
	// +   improved by: ntoniazzi (http://phpjs.org/functions/bin2hex:361#comment_177616)
	// *     example 1: bin2hex('Kev');
	// *     returns 1: '4b6576'
	// *     example 2: bin2hex(String.fromCharCode(0x00));
	// *     returns 2: '00'

	var i, l, o = "", n;

	s += "";

	for (i = 0, l = s.length; i < l; i++) {
	    n = s.charCodeAt(i).toString(16)
	    o += n.length < 2 ? "0" + n : n;
	}

	return o;
    }

    /**
     * export to either browser or node.js
     */
    if (typeof exports !== 'undefined') {
	if (typeof module !== "undefined" && module.exports){
	    // Node.js
	    exports = module.exports = IpatMarkSheetJRA
//	    var sprintf = require('sprintf');
	}else{
	    // Common.js
	    exports.IpatMarkSheetJRA = IpatMarkSheetJRA
//            exports.sprintf = sprintf
	}
    } else {
	// DOM
        window.IpatMarkSheetJRA = IpatMarkSheetJRA
        if (typeof define === 'function' && define.amd) {
            define(function() {
                return {
                    IpatMarkSheetJRA: IpatMarkSheetJRA
                }
            })
        }
    }
    
})(typeof window === 'undefined' ? this : window);



