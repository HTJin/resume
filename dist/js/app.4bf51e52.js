(function(e){function t(t){for(var o,a,s=t[0],l=t[1],c=t[2],u=0,p=[];u<s.length;u++)a=s[u],Object.prototype.hasOwnProperty.call(i,a)&&i[a]&&p.push(i[a][0]),i[a]=0;for(o in l)Object.prototype.hasOwnProperty.call(l,o)&&(e[o]=l[o]);d&&d(t);while(p.length)p.shift()();return r.push.apply(r,c||[]),n()}function n(){for(var e,t=0;t<r.length;t++){for(var n=r[t],o=!0,s=1;s<n.length;s++){var l=n[s];0!==i[l]&&(o=!1)}o&&(r.splice(t--,1),e=a(a.s=n[0]))}return e}var o={},i={app:0},r=[];function a(t){if(o[t])return o[t].exports;var n=o[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,a),n.l=!0,n.exports}a.m=e,a.c=o,a.d=function(e,t,n){a.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},a.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.t=function(e,t){if(1&t&&(e=a(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(a.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)a.d(n,o,function(t){return e[t]}.bind(null,o));return n},a.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return a.d(t,"a",t),t},a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},a.p="/resume/";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],l=s.push.bind(s);s.push=t,s=s.slice();for(var c=0;c<s.length;c++)t(s[c]);var d=l;r.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"1fdd":function(e,t,n){},"21bb":function(e,t,n){"use strict";var o=n("d63f"),i=n.n(o);i.a},"408d":function(e,t,n){"use strict";var o=n("50f1"),i=n.n(o);i.a},"50f1":function(e,t,n){},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var o=n("2b0e"),i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-app",[n("v-content",[n("transition",{attrs:{name:e.transitionName,mode:"out-in"}},[n("router-view")],1)],1)],1)},r=[],a=(n("ac1f"),n("1276"),{name:"App",data:function(){return{transitionName:""}},watch:{$route:function(e,t){var n=e.path.split("/timeline").length,o=t.path.split("/").length;this.transitionName=n<o?"slide-home":"slide-timeline"}}}),s=a,l=(n("5c0b"),n("2877")),c=n("6544"),d=n.n(c),u=n("7496"),p=n("a75b"),v=Object(l["a"])(s,i,r,!1,null,null,null),m=v.exports;d()(v,{VApp:u["a"],VContent:p["a"]});var f=n("8c4f"),h=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("v-container",{directives:[{name:"show",rawName:"v-show",value:e.visible,expression:"visible"}],staticClass:"home",attrs:{fluid:""}},[o("v-row",{staticClass:"mainbody"},[o("v-col",{attrs:{xl:"5",lg:"5",md:"5",sm:"5",xs:"6"}},[o("img",{staticClass:"face",attrs:{alt:"Muh face",src:n("7786")}})]),o("v-col",{attrs:{xl:"2",lg:"2",md:"2",sm:"2",xs:"1"}},[o("div",{staticClass:"split"})]),o("v-col",{attrs:{xl:"5",lg:"5",md:"5",sm:"5",xs:"6"}},[o("div",{staticClass:"link-buttons"},[o("h1",[e._v("Hyun-Tae Jin")]),o("div",{staticClass:"mdiIcons"},[o("a",{attrs:{target:"_blank",rel:"noopener noreferrer",href:"mailto:htjmario@gmail.com"}},[o("v-hover",{scopedSlots:e._u([{key:"default",fn:function(t){var n=t.hover;return[o("v-icon",{attrs:{id:"gmail",large:"",dark:"",color:n?"#CE493B":"#edf5e1"}},[e._v(e._s(e.mdiGmail))])]}}])}),o("v-tooltip",{attrs:{activator:"#gmail",bottom:"",color:"#05385B"}},[o("span",[e._v("htjmario@gmail.com")])])],1),o("v-icon",{attrs:{small:"",dark:""}},[e._v(e._s(e.mdiPowerOn))]),o("a",{attrs:{target:"_blank",rel:"noopener noreferrer",href:"https://github.com/HTJin"}},[o("v-hover",{scopedSlots:e._u([{key:"default",fn:function(t){var n=t.hover;return[o("v-icon",{attrs:{id:"github",large:"",dark:"",color:n?"#A66CFF":"#edf5e1"}},[e._v(e._s(e.mdiGithub))])]}}])}),o("v-tooltip",{attrs:{activator:"#github",bottom:"",color:"#05385B"}},[o("span",[e._v("github.com/htjin")])])],1),o("v-icon",{attrs:{small:"",dark:""}},[e._v(e._s(e.mdiPowerOn))]),o("a",{attrs:{target:"_blank",rel:"noopener noreferrer",href:"https://linkedin.com/in/HTJin"}},[o("v-hover",{scopedSlots:e._u([{key:"default",fn:function(t){var n=t.hover;return[o("v-icon",{attrs:{id:"linkedin",large:"",dark:"",color:n?"#0077B5":"#edf5e1"}},[e._v(e._s(e.mdiLinkedin))])]}}])}),o("v-tooltip",{attrs:{activator:"#linkedin",bottom:"",color:"#05385B"}},[o("span",[e._v("linkedin/in/HTJin")])])],1)],1)])])],1),o("div",{staticClass:"scroll"},[o("v-tooltip",{attrs:{top:"",color:"#5cdb95"},scopedSlots:e._u([{key:"activator",fn:function(t){var n=t.on;return[o("div",e._g({staticClass:"down",on:{click:e.determineVisible}},n),[o("router-link",{attrs:{to:"/timeline"}},[o("v-hover",{scopedSlots:e._u([{key:"default",fn:function(t){var n=t.hover;return[o("v-icon",{attrs:{large:"",dark:"",color:n?"#5cdb95":"#edf5e1"}},[e._v(e._s(n?e.mdiChevronTripleDown:e.mdiChevronDown))])]}}],null,!0)})],1)],1)]}}])},[o("span",[e._v("Timeline")])])],1)],1)},w=[],g=n("94ed"),b={name:"Home",computed:{visible:function(){return this.$store.state.visible}},methods:{determineVisible:function(){this.$store.commit("determineVisible")}},data:function(){return{mdiGithub:g["e"],mdiGmail:g["f"],mdiLinkedin:g["g"],mdiPowerOn:g["j"],mdiChevronDown:g["a"],mdiChevronTripleDown:g["b"]}}},_=b,k=(n("21bb"),n("62ad")),y=n("a523"),C=n("ce87"),S=n("132d"),P=n("0fd9"),x=n("3a2f"),O=Object(l["a"])(_,h,w,!1,null,null,null),j=O.exports;d()(O,{VCol:k["a"],VContainer:y["a"],VHover:C["a"],VIcon:S["a"],VRow:P["a"],VTooltip:x["a"]});var W=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-container",{directives:[{name:"show",rawName:"v-show",value:e.show,expression:"show"}],staticClass:"timeline",staticStyle:{height:"88vh"},attrs:{fluid:""}},[e.toggleSkills?e._e():n("div",{staticClass:"sections-container"},[n("v-col",{attrs:{xl:"8",lg:"8",md:"8",sm:"8",xs:"6"}},[n("Experience",{attrs:{section:e.ExpSection,windowWidth:e.windowWidth}})],1),n("v-col",{attrs:{xl:"1",lg:"1",md:"1",sm:"1",xs:"1"}},[e.windowWidth>600?n("div",{staticClass:"split"}):n("div",{staticClass:"toggle-over",on:{click:function(t){e.toggleSkills=!e.toggleSkills}}},e._l(5,(function(t){return n("v-icon",{key:t.id,attrs:{dark:"",color:"#5cdb95"}},[e._v(" "+e._s(e.mdiTransferRight)+" ")])})),1)]),e.windowWidth>600?n("v-col",{attrs:{xl:"8",lg:"8",md:"8",sm:"8",xs:"6"}},[n("Technical",{attrs:{section:e.TechSection,windowWidth:e.windowWidth}})],1):e._e()],1),e.toggleSkills?n("div",{staticClass:"sections-container"},[n("v-col",{attrs:{xl:"1",lg:"1",md:"1",sm:"1",xs:"1"}},[n("div",{staticClass:"toggle-over",on:{click:function(t){e.toggleSkills=!e.toggleSkills}}},e._l(5,(function(t){return n("v-icon",{key:t.id,attrs:{dark:"",color:"#5cdb95"}},[e._v(" "+e._s(e.mdiTransferLeft)+" ")])})),1)]),n("v-col",{attrs:{xl:"11",lg:"11",md:"11",sm:"11",xs:"11"}},[n("Technical",{attrs:{section:e.TechSection,windowWidth:e.windowWidth}})],1)],1):e._e(),n("div",{staticClass:"scroll"},[n("v-tooltip",{attrs:{top:"",color:"#5cdb95"},scopedSlots:e._u([{key:"activator",fn:function(t){var o=t.on;return[n("div",e._g({staticClass:"up",on:{click:e.determineShow}},o),[n("router-link",{attrs:{to:"/"}},[n("v-hover",{scopedSlots:e._u([{key:"default",fn:function(t){var o=t.hover;return[n("v-icon",{attrs:{large:"",dark:"",color:o?"#5cdb95":"#edf5e1"}},[e._v(e._s(o?e.mdiChevronTripleUp:e.mdiChevronUp))])]}}],null,!0)})],1)],1)]}}])},[n("span",[e._v("Back Up")])])],1)])},T=[],M=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-slide-x-transition",[n("div",{staticClass:"resume-container"},[n("v-hover",{scopedSlots:e._u([{key:"default",fn:function(t){var o=t.hover;return[n("span",{staticClass:"toggle",attrs:{id:"prof"},on:{click:function(t){e.profOpen=!e.profOpen}}},[n("v-icon",{staticClass:"drawer-up",attrs:{large:e.windowWidth>600,small:e.windowWidth<600,dark:"",color:e.profOpen?o?"#5cdb95":"#edf5e1":"#20688a"}},[e._v(e._s(e.mdiMenuUp))]),n("v-icon",{staticClass:"drawer-down",attrs:{large:e.windowWidth>600,small:e.windowWidth<600,dark:"",color:e.profOpen?"#20688a":o?"#5cdb95":"#edf5e1"}},[e._v(e._s(e.mdiMenuDown))])],1)]}}])}),n("v-tooltip",{attrs:{activator:"#prof",left:e.windowWidth>600,bottom:e.windowWidth<600,color:"#042D4A"}},[e._v(" "+e._s(e.profOpen?"Close":"Open")+" ")]),n("h1",[e._v("Professional Experience")]),e._l(e.sectionProfExp,(function(t){return n("div",{key:t.id},[n("h2",[e._v(e._s(t.job))]),n("h3",[e._v(" "+e._s(t.location)+" "),n("span",{staticClass:"year"},[e._v(e._s(t.year))])]),e._l(t.description,(function(t){return n("ul",{key:t.id,staticClass:"descProf"},[n("v-expand-transition",[n("li",{directives:[{name:"show",rawName:"v-show",value:e.profOpen,expression:"profOpen"}]},[e._v(e._s(t))])])],1)}))],2)})),n("v-hover",{scopedSlots:e._u([{key:"default",fn:function(t){var o=t.hover;return[n("span",{staticClass:"toggle",attrs:{id:"comm"},on:{click:function(t){e.commOpen=!e.commOpen}}},[n("v-icon",{staticClass:"drawer-up",attrs:{large:e.windowWidth>600,small:e.windowWidth<600,dark:"",color:e.commOpen?o?"#5cdb95":"#edf5e1":"#20688a"}},[e._v(e._s(e.mdiMenuUp))]),n("v-icon",{staticClass:"drawer-down",attrs:{large:e.windowWidth>600,small:e.windowWidth<600,dark:"",color:e.commOpen?"#20688a":o?"#5cdb95":"#edf5e1"}},[e._v(e._s(e.mdiMenuDown))])],1)]}}])}),n("v-tooltip",{attrs:{activator:"#comm",left:e.windowWidth>600,bottom:e.windowWidth<600,color:"#042D4A"}},[e._v(" "+e._s(e.commOpen?"Close":"Open")+" ")]),n("h1",[e._v("Community Involvement")]),e._l(e.sectionCommInv,(function(t){return n("div",{key:t.id},[n("h2",[e._v(e._s(t.job))]),n("h3",[e._v(" "+e._s(t.location)+" "),n("span",{staticClass:"year"},[e._v(e._s(t.year))])]),e._l(t.description,(function(t){return n("ul",{key:t.id,staticClass:"descComm"},[n("v-expand-transition",[n("li",{directives:[{name:"show",rawName:"v-show",value:e.commOpen,expression:"commOpen"}]},[e._v(e._s(t))])])],1)}))],2)})),n("v-hover",{scopedSlots:e._u([{key:"default",fn:function(t){var o=t.hover;return[n("span",{staticClass:"toggle",attrs:{id:"pers"},on:{click:function(t){e.persOpen=!e.persOpen}}},[n("v-icon",{staticClass:"drawer-up",attrs:{large:e.windowWidth>600,small:e.windowWidth<600,dark:"",color:e.persOpen?o?"#5cdb95":"#edf5e1":"#20688a"}},[e._v(e._s(e.mdiMenuUp))]),n("v-icon",{staticClass:"drawer-down",attrs:{large:e.windowWidth>600,small:e.windowWidth<600,dark:"",color:e.persOpen?"#20688a":o?"#5cdb95":"#edf5e1"}},[e._v(e._s(e.mdiMenuDown))])],1)]}}])}),n("v-tooltip",{attrs:{activator:"#pers",left:e.windowWidth>600,bottom:e.windowWidth<600,color:"#042D4A"}},[e._v(" "+e._s(e.persOpen?"Close":"Open")+" ")]),n("h1",[e._v("Personal Projects")]),e._l(e.sectionPersPro,(function(t){return n("div",{key:t.id},[n("h3",{staticClass:"projects"},[e._v(e._s(t.job))]),e._l(t.description,(function(t){return n("ul",{key:t.id,staticClass:"descPers"},[n("v-expand-transition",[n("li",{directives:[{name:"show",rawName:"v-show",value:e.persOpen,expression:"persOpen"}]},[e._v(e._s(t))])])],1)}))],2)}))],2)])},V=[],A=(n("4de4"),n("a9e3"),{name:"Experience",props:{section:Array,windowWidth:Number},data:function(){return{mdiMenuUp:g["i"],mdiMenuDown:g["h"],profOpen:!1,persOpen:!1,commOpen:!1}},computed:{sectionProfExp:function(){return this.section.filter((function(e){return"Professional Experience"===e.title}))},sectionPersPro:function(){return this.section.filter((function(e){return"Personal Projects"===e.title}))},sectionCommInv:function(){return this.section.filter((function(e){return"Community Involvement"===e.title}))}}}),E=A,U=(n("408d"),n("0789")),D=Object(l["a"])(E,M,V,!1,null,null,null),H=D.exports;d()(D,{VExpandTransition:U["a"],VHover:C["a"],VIcon:S["a"],VSlideXTransition:U["c"],VTooltip:x["a"]});var I=n("d036"),J=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-slide-x-reverse-transition",[n("div",{staticClass:"skills-container"},e._l(e.section,(function(t){return n("div",{key:t.id},[n("h1",[e._v(e._s(t.title))]),t.location?n("h3",[e._v(e._s(t.location))]):e._e(),e._l(t.skills,(function(t){return n("ul",{key:t.id,staticClass:"skill"},[n("li",[e._v(e._s(t))])])}))],2)})),0)])},N=[],R={name:"Technical",props:{section:Array}},B=R,G=(n("acc3"),Object(l["a"])(B,J,N,!1,null,null,null)),$=G.exports;d()(G,{VSlideXReverseTransition:U["b"]});var L=n("db8c"),z={name:"Timeline",components:{Experience:H,Technical:$},computed:{show:function(){return this.$store.state.show}},methods:{determineShow:function(){this.$store.commit("determineShow")}},data:function(){return{mdiChevronUp:g["d"],mdiChevronTripleUp:g["c"],mdiTransferLeft:g["k"],mdiTransferRight:g["l"],ExpSection:I,TechSection:L,windowWidth:window.innerWidth,toggleSkills:!1}},mounted:function(){var e=this;window.onresize=function(){e.windowWidth=window.innerWidth}}},F=z,K=(n("a932"),Object(l["a"])(F,W,T,!1,null,null,null)),q=K.exports;d()(K,{VCol:k["a"],VContainer:y["a"],VHover:C["a"],VIcon:S["a"],VTooltip:x["a"]}),o["a"].use(f["a"]);var Q=[{path:"/",name:"Home",component:j},{path:"/timeline",name:"Timeline",component:q}],X=new f["a"]({routes:Q}),Y=X,Z=n("2f62");o["a"].use(Z["a"]);var ee=new Z["a"].Store({state:{visible:!0,show:!0},mutations:{determineShow:function(e){e.show=!e.show,!0===e.show?e.visible=!1:e.visible=!0},determineVisible:function(e){e.visible=!e.visible,!0===e.visible?e.show=!1:e.show=!0}},actions:{},modules:{}}),te=n("f309");o["a"].use(te["a"]);var ne=new te["a"]({icons:{iconfont:"mdiSvg"}});o["a"].config.productionTip=!1,new o["a"]({router:Y,store:ee,vuetify:ne,render:function(e){return e(m)}}).$mount("#app")},"5c0b":function(e,t,n){"use strict";var o=n("7694"),i=n.n(o);i.a},7694:function(e,t,n){},7786:function(e,t,n){e.exports=n.p+"img/profile.b86556b0.jpeg"},a932:function(e,t,n){"use strict";var o=n("c1f6"),i=n.n(o);i.a},acc3:function(e,t,n){"use strict";var o=n("1fdd"),i=n.n(o);i.a},c1f6:function(e,t,n){},d036:function(e){e.exports=JSON.parse('[{"title":"Professional Experience","job":"Associate Applications Developer","location":"Highmark Health Solutions Inc., Pittsburgh, PA","year":"2019 - 2020","description":["Successfully delivered a web portal application using Vue.js and Java that makes inquiries/referrals to the Highmark providers","Was able to demonstrate the value and strength of Vue as a Javascript framework to the company and even had Github unblocked and moved to the company proxy whitelist","Main front end developer/architect for a scrum team, led and determined story points for AGILE sprints","Used PegaSystems Platform to maintain and develop Highmark\'s Utilization Management tool, which gets used by Highmark hospital\'s doctors and nurses"]},{"title":"Professional Experience","job":"Junior Web Developer","location":"Checkmate Digital, New Haven, CT","year":"2018 - 2019","description":["Worked remotely from Pittsburgh on client to client projects","Gained front end experience working with Javascript frameworks, exposing myself to a variety of projects depending on the client","Learned the importance of proper Git version control and adapted to company’s Git flow","Contributed to 4 unique projects"]},{"title":"Personal Projects","job":"Rift - Public Repository: https://github.com/OpenLeagueSeries/Rift/","description":["Registration application for a popular video gaming club at University of Pittsburgh","Created with React.js and was formerly deployed at https://pitt.lol","Recruited and taught students on using React and Git. Made a tutorial video at https://www.twitch.tv/videos/273200884"]},{"title":"Personal Projects","job":"Password Evaluation and Cracker","description":["Password cracking program created with Java","Uses a given dictionary.txt file with words and evaluates the strength of passwords","Implemented MD5 Hash for cracking passwords"]},{"title":"Personal Projects","job":"Restaurant Website","description":["Website for a restaurant created with HTML, CSS, and JavaScript","Users can make reservations, order from a menu and add to shopping cart, then make transactions online","Implemented Google maps API to display \\"location\\" of the restaurant, and Paypal API for transactions"]},{"title":"Personal Projects","job":"Forum Website","description":["Created an online forum with PHP and MySQL database where users can post a topic, comments, and replies to one another"]},{"title":"Personal Projects","job":"University of Pittsburgh Mobile App Proposal","description":["Designed a University of Pittsburgh mobile application and presented a paper model demo to the school’s web administrator"]},{"title":"Community Involvement","job":"Coordinator & Co-Founder","location":"Pitt Smash Bros. Club - University of Pittsburgh","year":"2014 - 2015","description":["Established a video gaming community on campus by creating events to play Super Smash Bros. on campus","Co-coordinated national size tournaments that over 288 unique entrants participated in","Set up live broadcasts for streaming online through popular website platform, www.twitch.tv"]},{"title":"Community Involvement","job":"Media Communications Chair","location":"Korean Culture Association - University of Pittsburgh","year":"2012 - 2013","description":["A cultural organization on campus to promote Korean culture on campus; ~400+ body members at large and ~14 executive officers","Managed organizational budget (~$22K) with Business Manager to host speakers, performers, and cultural events","Collaborated in weekly executive board meetings; served as organizational representative to monthly cross-organizational meetings and networking events"]},{"title":"Community Involvement","job":"Founding Member","location":"iDEAS Conference - University of Pittsburgh","year":"2011 - 2012","description":["Focused on creating a solid management and leadership structure for CMU and PITT","Helped develop the mission statement and vision for the structure of the conference","Created the conference description and conference structure","Co-created the Marketing Plan which outlines the necessary steps for a successful conference"]}]')},d63f:function(e,t,n){},db8c:function(e){e.exports=JSON.parse('[{"title":"Skills","skills":["VueJS, Vuex, Axios","ReactJS, Redux","AngularJS, TypeScript","Polymer/lit-element","Vuetify, Material-UI, Bootstrap","Python, Java","PHP, MySQL","HTML, SCSS, CSS","Pega 6.3/Pega 8.2"]},{"title":"Education","location":"University of Pittsburgh, Pittsburgh, PA","skills":["Bachelor of Science in Information Science","Concentrated Area in Networks and Security","Related Area/Minor in Computer Science","Graduated December 2016"]},{"title":"Coursework","skills":["Web Programming","Website Design/Development","Human Factors in Systems Design","Computer Security","Database Management Systems","Analysis of Information Systems","Telecommunications & Networks","Applications of Networks","Wireless Networks"]},{"title":"Citizenship/Work Authorization","location":"US Citizen","skills":["Bilingual in English and Korean"]}]')}});
//# sourceMappingURL=app.4bf51e52.js.map