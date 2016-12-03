(function (){ var f="function",l="object",m,n=this,p=function(a){var b=typeof a;if(b==l)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return l;if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return f}else return"null";
else if(b==f&&"undefined"==typeof a.call)return l;return b},q=function(a){return"string"==typeof a},r=function(a,b){function c(){}c.prototype=b.prototype;a.ca=b.prototype;a.prototype=new c;a.ba=function(a,c,g){for(var d=Array(arguments.length-2),e=2;e<arguments.length;e++)d[e-2]=arguments[e];return b.prototype[c].apply(a,d)}};var t=function(a){if(Error.captureStackTrace)Error.captureStackTrace(this,t);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))};r(t,Error);var aa=function(a,b){for(var c=a.split("%s"),d="",e=Array.prototype.slice.call(arguments,1);e.length&&1<c.length;)d+=c.shift()+e.shift();return d+c.join("%s")},u=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^[\s\xa0]+|[\s\xa0]+$/g,"")},v=function(a,b){return a<b?-1:a>b?1:0};var w=function(a,b){b.unshift(a);t.call(this,aa.apply(null,b));b.shift()};r(w,t);var x=function(a,b,c,d){var e="Assertion failed";if(c)var e=e+(": "+c),g=d;else a&&(e+=": "+a,g=b);throw new w(""+e,g||[]);},y=function(a,b,c){a||x("",null,b,Array.prototype.slice.call(arguments,2));return a},z=function(a,b,c){"number"==typeof a||x("Expected number but got %s: %s.",[p(a),a],b,Array.prototype.slice.call(arguments,2));return a};var ba=Array.prototype.indexOf?function(a,b,c){y(null!=a.length);return Array.prototype.indexOf.call(a,b,c)}:function(a,b,c){c=null==c?0:0>c?Math.max(0,a.length+c):c;if(q(a))return q(b)&&1==b.length?a.indexOf(b,c):-1;for(;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},A=function(a){return Array.prototype.concat.apply(Array.prototype,arguments)},ca=function(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]};var B;a:{var C=n.navigator;if(C){var D=C.userAgent;if(D){B=D;break a}}B=""};var da=function(a,b,c,d){d=d?d(b):b;return Object.prototype.hasOwnProperty.call(a,d)?a[d]:a[d]=c(b)};var ea=-1!=B.indexOf("Opera"),E=-1!=B.indexOf("Trident")||-1!=B.indexOf("MSIE"),fa=-1!=B.indexOf("Edge"),F=-1!=B.indexOf("Gecko")&&!(-1!=B.toLowerCase().indexOf("webkit")&&-1==B.indexOf("Edge"))&&!(-1!=B.indexOf("Trident")||-1!=B.indexOf("MSIE"))&&-1==B.indexOf("Edge"),ga=-1!=B.toLowerCase().indexOf("webkit")&&-1==B.indexOf("Edge"),G=function(){var a=n.document;return a?a.documentMode:void 0},H;
a:{var I="",J=function(){var a=B;if(F)return/rv\:([^\);]+)(\)|;)/.exec(a);if(fa)return/Edge\/([\d\.]+)/.exec(a);if(E)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(ga)return/WebKit\/(\S+)/.exec(a);if(ea)return/(?:Version)[ \/]?(\S+)/.exec(a)}();J&&(I=J?J[1]:"");if(E){var K=G();if(null!=K&&K>parseFloat(I)){H=String(K);break a}}H=I}
var L=H,ha={},M=function(a){return da(ha,a,function(){for(var b=0,c=u(String(L)).split("."),d=u(String(a)).split("."),e=Math.max(c.length,d.length),g=0;0==b&&g<e;g++){var h=c[g]||"",k=d[g]||"";do{h=/(\d*)(\D*)(.*)/.exec(h)||["","","",""];k=/(\d*)(\D*)(.*)/.exec(k)||["","","",""];if(0==h[0].length&&0==k[0].length)break;b=v(0==h[1].length?0:parseInt(h[1],10),0==k[1].length?0:parseInt(k[1],10))||v(0==h[2].length,0==k[2].length)||v(h[2],k[2]);h=h[3];k=k[3]}while(0==b)}return 0<=b})},N=n.document,ia=N&&
E?G()||("CSS1Compat"==N.compatMode?parseInt(L,10):5):void 0;!F&&!E||E&&9<=Number(ia)||F&&M("1.9.1");E&&M("9");var ja=function(a,b){return q(b)?a.getElementById(b):b},ka=function(a,b,c,d){a=d||a;var e=b&&"*"!=b?String(b).toUpperCase():"";if(a.querySelectorAll&&a.querySelector&&(e||c))return a.querySelectorAll(e+(c?"."+c:""));if(c&&a.getElementsByClassName){b=a.getElementsByClassName(c);if(e){a={};for(var g=d=0,h;h=b[g];g++)e==h.nodeName&&(a[d++]=h);a.length=d;return a}return b}b=a.getElementsByTagName(e||"*");if(c){a={};for(g=d=0;h=b[g];g++){var e=h.className,k;if(k=typeof e.split==f)k=0<=ba(e.split(/\s+/),
c);k&&(a[d++]=h)}a.length=d;return a}return b},la=function(a){y(a,"Node cannot be null or undefined.");return 9==a.nodeType?a:a.ownerDocument||a.document};var O=function(a){this.D=a};O.prototype.serialize=function(a){var b=[];this.H(a,b);return b.join("")};
O.prototype.H=function(a,b){if(null==a)b.push("null");else{if(typeof a==l){if("array"==p(a)){this.serializeArray(a,b);return}if(a instanceof String||a instanceof Number||a instanceof Boolean)a=a.valueOf();else{this.Z(a,b);return}}switch(typeof a){case "string":this.L(a,b);break;case "number":this.Y(a,b);break;case "boolean":b.push(String(a));break;case f:b.push("null");break;default:throw Error("Unknown type: "+typeof a);}}};
var ma={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},na=/\uffff/.test("\uffff")?/[\\\"\x00-\x1f\x7f-\uffff]/g:/[\\\"\x00-\x1f\x7f-\xff]/g;O.prototype.L=function(a,b){b.push('"',a.replace(na,function(a){var b=ma[a];b||(b="\\u"+(a.charCodeAt(0)|65536).toString(16).substr(1),ma[a]=b);return b}),'"')};O.prototype.Y=function(a,b){b.push(isFinite(a)&&!isNaN(a)?String(a):"null")};
O.prototype.serializeArray=function(a,b){var c=a.length;b.push("[");for(var d="",e=0;e<c;e++)b.push(d),d=a[e],this.H(this.D?this.D.call(a,String(e),d):d,b),d=",";b.push("]")};O.prototype.Z=function(a,b){b.push("{");var c="",d;for(d in a)if(Object.prototype.hasOwnProperty.call(a,d)){var e=a[d];typeof e!=f&&(b.push(c),this.L(d,b),b.push(":"),this.H(this.D?this.D.call(a,d,e):e,b),c=",")}b.push("}")};var oa="StopIteration"in n?n.StopIteration:{message:"StopIteration",stack:""},P=function(){};P.prototype.next=function(){throw oa;};P.prototype.T=function(){return this};var Q=function(a,b){this.g={};this.c=[];this.F=this.b=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else a&&this.addAll(a)};m=Q.prototype;m.o=function(){this.A();for(var a=[],b=0;b<this.c.length;b++)a.push(this.g[this.c[b]]);return a};m.v=function(){this.A();return this.c.concat()};m.u=function(a){return R(this.g,a)};
m.remove=function(a){return R(this.g,a)?(delete this.g[a],this.b--,this.F++,this.c.length>2*this.b&&this.A(),!0):!1};m.A=function(){if(this.b!=this.c.length){for(var a=0,b=0;a<this.c.length;){var c=this.c[a];R(this.g,c)&&(this.c[b++]=c);a++}this.c.length=b}if(this.b!=this.c.length){for(var d={},b=a=0;a<this.c.length;)c=this.c[a],R(d,c)||(this.c[b++]=c,d[c]=1),a++;this.c.length=b}};m.get=function(a,b){return R(this.g,a)?this.g[a]:b};
m.set=function(a,b){R(this.g,a)||(this.b++,this.c.push(a),this.F++);this.g[a]=b};m.addAll=function(a){var b;if(a instanceof Q)b=a.v(),a=a.o();else{b=[];var c=0,d;for(d in a)b[c++]=d;c=[];d=0;for(var e in a)c[d++]=a[e];a=c}for(e=0;e<b.length;e++)this.set(b[e],a[e])};m.forEach=function(a,b){for(var c=this.v(),d=0;d<c.length;d++){var e=c[d],g=this.get(e);a.call(b,g,e,this)}};m.clone=function(){return new Q(this)};
m.T=function(a){this.A();var b=0,c=this.F,d=this,e=new P;e.next=function(){if(c!=d.F)throw Error("The map has changed since the iterator was created");if(b>=d.c.length)throw oa;var e=d.c[b++];return a?e:d.g[e]};return e};var R=function(a,b){return Object.prototype.hasOwnProperty.call(a,b)};var pa=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/,qa=function(a,b){if(a)for(var c=a.split("&"),d=0;d<c.length;d++){var e=c[d].indexOf("="),g,h=null;0<=e?(g=c[d].substring(0,e),h=c[d].substring(e+1)):g=c[d];b(g,h?decodeURIComponent(h.replace(/\+/g," ")):"")}};var S=function(a,b){this.B=this.J=this.s="";this.C=null;this.G=this.K="";this.f=this.X=!1;var c;a instanceof S?(this.f=void 0!==b?b:a.f,this.R(a.s),this.S(a.J),this.M(a.B),this.O(a.C),this.setPath(a.getPath()),this.P(a.h.clone()),this.N(a.G)):a&&(c=String(a).match(pa))?(this.f=!!b,this.R(c[1]||"",!0),this.S(c[2]||"",!0),this.M(c[3]||"",!0),this.O(c[4]),this.setPath(c[5]||"",!0),this.P(c[6]||"",!0),this.N(c[7]||"",!0)):(this.f=!!b,this.h=new T(null,null,this.f))};m=S.prototype;
m.toString=function(){var a=[],b=this.s;b&&a.push(U(b,ra,!0),":");var c=this.B;if(c||"file"==b)a.push("//"),(b=this.J)&&a.push(U(b,ra,!0),"@"),a.push(encodeURIComponent(String(c)).replace(/%25([0-9a-fA-F]{2})/g,"%$1")),c=this.C,null!=c&&a.push(":",String(c));if(c=this.getPath())this.W()&&"/"!=c.charAt(0)&&a.push("/"),a.push(U(c,"/"==c.charAt(0)?sa:ta,!0));(c=this.U())&&a.push("?",c);(c=this.G)&&a.push("#",U(c,ua));return a.join("")};m.clone=function(){return new S(this)};
m.R=function(a,b){this.j();if(this.s=b?V(a,!0):a)this.s=this.s.replace(/:$/,"");return this};m.S=function(a,b){this.j();this.J=b?V(a):a;return this};m.M=function(a,b){this.j();this.B=b?V(a,!0):a;return this};m.W=function(){return!!this.B};m.O=function(a){this.j();if(a){a=Number(a);if(isNaN(a)||0>a)throw Error("Bad port number "+a);this.C=a}else this.C=null;return this};m.getPath=function(){return this.K};m.setPath=function(a,b){this.j();this.K=b?V(a,!0):a;return this};
m.P=function(a,b){this.j();a instanceof T?(this.h=a,this.h.I(this.f)):(b||(a=U(a,va)),this.h=new T(a,null,this.f));return this};m.U=function(){return this.h.toString()};m.aa=function(a,b){this.j();this.h.set(a,b);return this};m.V=function(a){return this.h.get(a)};m.N=function(a,b){this.j();this.G=b?V(a):a;return this};m.j=function(){if(this.X)throw Error("Tried to modify a read-only Uri");};m.I=function(a){this.f=a;this.h&&this.h.I(a);return this};
var V=function(a,b){return a?b?decodeURI(a.replace(/%25/g,"%2525")):decodeURIComponent(a):""},U=function(a,b,c){return q(a)?(a=encodeURI(a).replace(b,wa),c&&(a=a.replace(/%25([0-9a-fA-F]{2})/g,"%$1")),a):null},wa=function(a){a=a.charCodeAt(0);return"%"+(a>>4&15).toString(16)+(a&15).toString(16)},ra=/[#\/\?@]/g,ta=/[\#\?:]/g,sa=/[\#\?]/g,va=/[\#\?@]/g,ua=/#/g,T=function(a,b,c){this.b=this.a=null;this.i=a||null;this.f=!!c};m=T.prototype;
m.l=function(){if(!this.a&&(this.a=new Q,this.b=0,this.i)){var a=this;qa(this.i,function(b,c){a.add(decodeURIComponent(b.replace(/\+/g," ")),c)})}};m.add=function(a,b){this.l();this.w();a=this.m(a);var c=this.a.get(a);c||this.a.set(a,c=[]);c.push(b);this.b=z(this.b)+1;return this};m.remove=function(a){this.l();a=this.m(a);return this.a.u(a)?(this.w(),this.b=z(this.b)-this.a.get(a).length,this.a.remove(a)):!1};m.u=function(a){this.l();a=this.m(a);return this.a.u(a)};
m.v=function(){this.l();for(var a=this.a.o(),b=this.a.v(),c=[],d=0;d<b.length;d++)for(var e=a[d],g=0;g<e.length;g++)c.push(b[d]);return c};m.o=function(a){this.l();var b=[];if(q(a))this.u(a)&&(b=A(b,this.a.get(this.m(a))));else{a=this.a.o();for(var c=0;c<a.length;c++)b=A(b,a[c])}return b};m.set=function(a,b){this.l();this.w();a=this.m(a);this.u(a)&&(this.b=z(this.b)-this.a.get(a).length);this.a.set(a,[b]);this.b=z(this.b)+1;return this};
m.get=function(a,b){var c=a?this.o(a):[];return 0<c.length?String(c[0]):b};m.setValues=function(a,b){this.remove(a);0<b.length&&(this.w(),this.a.set(this.m(a),ca(b)),this.b=z(this.b)+b.length)};m.toString=function(){if(this.i)return this.i;if(!this.a)return"";for(var a=[],b=this.a.v(),c=0;c<b.length;c++)for(var d=b[c],e=encodeURIComponent(String(d)),d=this.o(d),g=0;g<d.length;g++){var h=e;""!==d[g]&&(h+="="+encodeURIComponent(String(d[g])));a.push(h)}return this.i=a.join("&")};
m.w=function(){this.i=null};m.clone=function(){var a=new T;a.i=this.i;this.a&&(a.a=this.a.clone(),a.b=this.b);return a};m.m=function(a){a=String(a);this.f&&(a=a.toLowerCase());return a};m.I=function(a){a&&!this.f&&(this.l(),this.w(),this.a.forEach(function(a,c){var b=c.toLowerCase();c!=b&&(this.remove(c),this.setValues(b,a))},this));this.f=a};var xa=function(a,b,c){var d;a:{d=la(b);if(d.defaultView&&d.defaultView.getComputedStyle&&(d=d.defaultView.getComputedStyle(b,null))){d=d[a]||d.getPropertyValue(a)||"";break a}d=""}d=d||(b.currentStyle?b.currentStyle[a]:null)||b.style&&b.style[a];return null==d||"inherit"==d||"transparent"==d||"rgba(0, 0, 0, 0)"==d?(d=la(b),b!=d.body&&b.parentNode?W(a,b.parentNode):c):d},W=function(a,b){return xa(a,b,"rgb(0, 0, 0)")},ya=function(){for(var a=ka(document,"iframe","blogger-iframe-colorize",void 0),b=
0;b<a.length;b++){var c=a[b],d=ja(document,c.id+"-src"),e=d.href;if(!(new S(e)).V("skin")){var g=W("color",c),h=W("backgroundColor",c),k=xa("fontFamily",c,"serif");d.href="https://www.blogger.com/unvisited-link-"+(new Date).valueOf();var Aa=W("color",d),d=d.href=e,e=encodeURIComponent,g=(new O(void 0)).serialize({color:g,backgroundColor:h,unvisitedLinkColor:Aa,fontFamily:k}),e=d+("#"+e(g))}c.src=e}};var za=!E;var Ba=-1;var Ca=function(){Ba=Math.floor(1E7*Math.random());for(var a=ka(document,"iframe","blogger-comment-from-post",void 0),b=0;b<a.length;b++){var c=ja(document,a[b].id+"-src"),d=new S(c.href);d.aa("blogspotRpcToken",Ba);c.href=d.toString()}ya();a=function(a){if(0==a.data.indexOf("set-comment-editor-height")){var b=document.getElementById("comment-editor");b.height=a.data.substring(26);za&&b.dataset?b.dataset.resized=!0:b.setAttribute("data-"+"resized".replace(/([A-Z])/g,"-$1").toLowerCase(),!0)}};window.addEventListener?
window.addEventListener("message",a,!1):window.attachEvent&&window.attachEvent("onmessage",a)},X=["BLOG_CMT_createIframe"],Y=n;X[0]in Y||!Y.execScript||Y.execScript("var "+X[0]);for(var Z;X.length&&(Z=X.shift());)X.length||void 0===Ca?Y=Y[Z]?Y[Z]:Y[Z]={}:Y[Z]=Ca; })()