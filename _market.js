/* ------------------------------------------------------------------ market
   Six figures drawn from the same records the other views read. Every chart
   is a plain SVG built here: one hue for magnitude (ink, with grey for a
   Partly), the accent only where it already means the third count, a table
   under each chart, and a tooltip on every mark. Nothing is estimated; a firm
   with no published figure is absent and the caption says how many that is. */
var MK=D.market||{};
function fmt(n){return String(n).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
/* Build 66. A chart is drawn in a fixed coordinate box and scaled to the
   column, so at 1440 its labels grew past body text and at 390 they fell to
   4 to 6 px. It now stops growing at its drawn width. On a phone the table
   under it opens by default, because the table is the readable form there. */
var NARROW=window.matchMedia&&window.matchMedia('(max-width:760px)').matches;
/* Build 78. On a phone every chart is drawn again at the column's own width,
   one unit to one pixel, with its labels above the bars instead of beside
   them. Before this each one was a 855px drawing behind a sideways scroll, so
   a reader saw 40 per cent of it: bars without their values, a map without
   its eastern counties, links running off the edge. */
/* The column is the viewport less the page gutter: 16px a side up to 640px,
   28px above. Measured when the charts are drawn, and again after a rotate. */
function colW(){var vw=document.documentElement.clientWidth||390;return vw-(vw<=640?32:56);}
var CW=NARROW?Math.max(288,Math.min(720,colW())):0;
function sizeCharts(){
  NARROW=window.matchMedia&&window.matchMedia('(max-width:760px)').matches;
  CW=NARROW?Math.max(288,Math.min(720,colW())):0;}
(function(){var last=null,t=null;
  window.addEventListener('resize',function(){clearTimeout(t);t=setTimeout(function(){
    var k=(window.matchMedia('(max-width:760px)').matches?'n':'w')+colW();
    if(k===last) return; last=k;
    var mk=document.getElementById('mkBody'); if(mk&&mk.innerHTML) drawMarket();},160);});})();
function svgOpen(w,h,cls){return '<svg class="fig'+(cls?' '+cls:'')+'" viewBox="0 0 '+w+' '+h+
  '" width="100%" style="max-width:'+w+'px'+(NARROW&&cls!=='map'&&w>CW+2?';min-width:'+Math.round(w*0.95)+'px':'')+
  '" preserveAspectRatio="xMinYMin meet" role="img" aria-hidden="false">';}
function tipAttr(t){return ' data-tip="'+esc(t)+'"';}

/* 1. Published annual closings, one bar per firm, with the machine-fit bands. */
var NB=(D.market&&D.market.closings_base)||0;
function figClosings(){
  var rows=MK.closings||[]; if(!rows.length) return '';
  var ph=NARROW, W=ph?CW:900,L=ph?0:190,R=ph?88:110,rowH=ph?40:30,top=ph?10:26,lab=ph?16:0,H=top+rows.length*rowH+30;
  /* Two builders close several times what the rest do. A linear axis to 6,362
     would flatten twenty bars into the first fifth of the chart, so the axis
     stops at 2,000 and a bar that runs past it is broken, with its full figure
     printed. Nothing is drawn at a length it does not have without saying so. */
  var max=2000, X=function(v){return L+(W-L-R)*Math.min(v,max)/max;};
  var h=svgOpen(W,H);
  // gridlines
  (ph?[0,500,1000,1500,2000]:[0,250,500,750,1000,1250,1500,1750,2000]).forEach(function(v){
    h+='<line x1="'+X(v)+'" y1="'+(top-8)+'" x2="'+X(v)+'" y2="'+(top+rows.length*rowH)+'" class="grid"/>'+
       '<text x="'+X(v)+'" y="'+(top+rows.length*rowH+18)+'" class="axt">'+fmt(v)+'</text>';
  });
  rows.forEach(function(r,i){
    var y0=top+i*rowH, y=y0+lab, bh=ph?14:18, cy=y+bh/2;
    var tip=r.name+': '+(r.over?'over ':'')+(r.low===r.high?fmt(r.high):fmt(r.low)+' to '+fmt(r.high))+
            ' homes a year, '+r.year+(r.wide?', '+r.wide:'')+'. '+r.source+'.';
    h+=ph?'<text x="0" y="'+(y0+11)+'" class="rowl" data-id="'+r.id+'">'+esc(r.short)+'</text>'
         :'<text x="'+(L-10)+'" y="'+(cy+4)+'" class="rowl" text-anchor="end" data-id="'+r.id+'">'+esc(r.short)+'</text>';
    h+='<rect x="'+X(0)+'" y="'+y+'" width="'+(X(r.low)-X(0))+'" height="'+bh+'" rx="0" class="bar"'+tipAttr(tip)+'/>';
    if(r.low>max){var bx=X(max)-22;
      h+='<path class="brk" d="M'+bx+' '+(y+bh+3)+' L'+(bx+7)+' '+(y-3)+' M'+(bx+7)+' '+(y+bh+3)+' L'+(bx+14)+' '+(y-3)+'"/>';}
    if(r.high>r.low){
      h+='<line x1="'+X(r.low)+'" y1="'+cy+'" x2="'+X(r.high)+'" y2="'+cy+'" class="range"'+tipAttr(tip)+'/>'+
         '<line x1="'+X(r.high)+'" y1="'+(cy-5)+'" x2="'+X(r.high)+'" y2="'+(cy+5)+'" class="range"/>';
    }
    h+='<text x="'+(X(r.high)+8)+'" y="'+(cy+4)+'" class="val">'+
       (r.over?'over ':'')+(r.low===r.high?fmt(r.high):fmt(r.low)+'–'+fmt(r.high))+(r.wide?'†':'')+' <tspan class="yr">'+r.year+'</tspan></text>';
  });
  h+='</svg>';
  var nw=rows.filter(function(r){return r.wide;}).length;
  var tbl='<table class="ftab"><thead><tr><th>Firm</th><th class="num">Homes a year</th><th>Year</th><th>Covers</th><th>Source</th></tr></thead><tbody>'+
    rows.map(function(r){return '<tr><td>'+esc(r.name)+'</td><td class="num">'+(r.over?'over ':'')+(r.low===r.high?fmt(r.high):fmt(r.low)+' to '+fmt(r.high))+
      '</td><td>'+r.year+'</td><td>'+esc(r.wide||PL.name)+'</td><td>'+esc(r.source)+'</td></tr>';}).join('')+'</tbody></table>';
  return figure('Homes closed a year, as published',
    rows.length+' of '+NB+' builders and developers publish a figure. The rest are not drawn. Axis stops at 2,000: a broken bar runs past it.'+
    (nw?' † '+nw+' figures cover more than '+PL.name+'.':''),
    h, tbl, null, 'figClosings',
    (D.bands_method&&D.bands_method.text?'<div class="bandnote"><span class="lab">The printer-fit bands</span><p>'+
      esc(D.bands_method.text)+'</p><p class="figsrc">'+(D.bands_method.sources||[]).map(function(s){
        return '<a class="src" href="'+esc(s.url)+'" target="_blank" rel="noopener">'+esc(s.label)+'</a>';}).join('')+
      '</p></div>':''));
}

/* 2. Track record and named decision-makers, by section. */
function figSections(){
  var rows=MK.by_section||[]; if(!rows.length) return '';
  var ph=NARROW, W=ph?CW:900,L=ph?0:230,R=ph?36:40,rowH=ph?46:34,top=ph?8:30,lab=ph?18:0,H=top+rows.length*rowH+12;
  var max=Math.max.apply(null,rows.map(function(r){return r.n;}));
  var X=function(v){return (W-L-R)*v/max;};
  var h=svgOpen(W,H);
  rows.forEach(function(r,i){
    var y=top+i*rowH+lab,bh=20,x=L;
    h+=ph?'<text x="0" y="'+(y-6)+'" class="rowl">'+esc(r.label)+'</text>'
         :'<text x="'+(L-10)+'" y="'+(y+14)+'" class="rowl" text-anchor="end">'+esc(r.label)+'</text>';
    [['yes','Yes','clear'],['partly','Partly','partial'],['no','No','fail']].forEach(function(s){
      var w=X(r[s[0]]); if(w<=0) return;
      var tip=r.label+': '+r[s[0]]+' of '+r.n+' with track record '+s[1]+'.';
      h+='<rect x="'+x+'" y="'+y+'" width="'+Math.max(0,w-2)+'" height="'+bh+'" class="seg '+s[2]+
         '" data-seg="'+r.group+':'+s[2]+'" tabindex="0" role="button" aria-label="'+esc(tip+' Show the firms.')+'"'+tipAttr(tip+' Click for the firms.')+'/>';
      if(w>=18) h+='<text x="'+(x+w/2-1)+'" y="'+(y+14)+'" class="segl '+s[2]+'" text-anchor="middle">'+r[s[0]]+'</text>';
      x+=w;
    });
    h+='<text x="'+(L+X(r.n)+8)+'" y="'+(y+14)+'" class="val">'+r.n+'</text>';
  });
  h+='</svg>';
  var leg='<div class="flegend"><i><span class="sw o"></span>Yes</i><i><span class="sw p"></span>Partly</i><i><span class="sw"></span>No</i></div>';
  var tbl='<table class="ftab"><thead><tr><th>Section</th><th>Firms</th><th>Record Yes</th><th>Partly</th><th>No</th><th>Decision-maker named</th><th>To confirm</th><th>With a link</th></tr></thead><tbody>'+
    rows.map(function(r){return '<tr><td>'+esc(r.label)+'</td><td>'+r.n+'</td><td>'+r.yes+'</td><td>'+r.partly+'</td><td>'+r.no+'</td><td>'+r.decider+'</td><td>'+r.confirm+'</td><td>'+r.linked+'</td></tr>';}).join('')+
    '</tbody></table>';
  return figure('Track record by section',
    'One bar per section, one segment per verdict. A segment lists its firms.',
    leg+h+'<div class="seglist" id="segList" hidden></div>', tbl);
}

/* 3. Land owners and the builders inside their communities. */
function figOwners(){
  var owners=(MK.owners||[]).map(function(o){return {id:o.id,short:o.short,line:o.line,
    builders:o.builders.filter(function(b){return b.id;})};}).filter(function(o){return o.builders.length;});
  if(!owners.length) return '';
  var names=[];owners.forEach(function(o){o.builders.forEach(function(b){if(names.indexOf(b.name)<0)names.push(b.name);});});
  var W=900,colL=230,colR=W-260,rowH=30,top=24;
  var H=top+Math.max(owners.length,names.length)*rowH+10;
  var yo=function(i){return top+i*rowH+(Math.max(0,names.length-owners.length)*rowH/2);};
  var yb=function(i){return top+i*rowH+(Math.max(0,owners.length-names.length)*rowH/2);};
  var h=svgOpen(W,H,'bip');
  owners.forEach(function(o,i){
    o.builders.forEach(function(b){
      var j=names.indexOf(b.name);
      var x1=colL+10,y1=yo(i)+10,x2=colR-10,y2=yb(j)+10,cx=(x1+x2)/2;
      h+='<path d="M'+x1+' '+y1+' C'+cx+' '+y1+' '+cx+' '+y2+' '+x2+' '+y2+'" class="link"'+
         tipAttr(b.name+' builds inside '+o.short+'.')+'/>';
    });
  });
  owners.forEach(function(o,i){
    h+='<text x="'+colL+'" y="'+(yo(i)+14)+'" class="node" text-anchor="end" data-id="'+o.id+'"'+
       tipAttr(o.line)+'>'+esc(o.short)+' <tspan class="cnt">'+o.builders.length+'</tspan></text>';
  });
  names.forEach(function(nm,j){
    var id=null; owners.forEach(function(o){o.builders.forEach(function(b){if(b.name===nm&&b.id)id=b.id;});});
    h+='<text x="'+colR+'" y="'+(yb(j)+14)+'" class="node'+(id?'':' off')+'"'+(id?' data-id="'+id+'"':'')+'>'+esc(nm)+
       '</text>';
  });
  h+='</svg>';
  /* Build 78. Two columns of names with curves between them need about 700px.
     On a phone the same pairs are a list: each owner, then the builders inside
     its communities. A builder on the deck opens its firm. */
  if(NARROW){
    h='<div class="oblist">'+owners.map(function(o){
      return '<div class="ob"><div class="obh"><button class="obn" data-id="'+o.id+'">'+esc(o.short)+
        '</button><span class="obc">'+o.builders.length+(o.builders.length===1?' builder':' builders')+'</span></div>'+
        '<div class="chips">'+o.builders.map(function(b){
          return b.id?'<button class="chip" data-id="'+b.id+'">'+esc(b.name)+'</button>'
            :'<span class="chip off">'+esc(b.name)+'</span>';
        }).join('')+'</div></div>';}).join('')+'</div>';
  }
  var tbl='<table class="ftab"><thead><tr><th>Land owner</th><th>Communities</th><th>Builders on this deck</th></tr></thead><tbody>'+
    owners.map(function(o){return '<tr><td>'+esc(o.short)+'</td><td>'+esc(o.line)+'</td><td>'+
      o.builders.map(function(b){return esc(b.name);}).join(', ')+'</td></tr>';}).join('')+'</tbody></table>';
  return figure('Land owners and the builders inside their communities',
    (NARROW?'Each masterplan owner, then the builders it lists that are on this deck.'
      :'Left: masterplan owners. Right: the builders each lists that are on this deck.'),
    h, tbl);
}

/* 4. Printed homes in Texas, on the public record. */
function figPrinted(){
  var rows=MK.printed||[]; if(!rows.length) return '';
  var ph=NARROW, W=ph?CW:900,L=ph?0:230,R=ph?112:150,rowH=ph?40:30,top=ph?6:12,lab=ph?16:0,H=top+rows.length*rowH+30;
  var max=Math.max.apply(null,rows.map(function(r){return r.units;}))||1;
  var X=function(v){return L+(W-L-R)*v/max;};
  var h=svgOpen(W,H);
  [0,25,50,75,100].forEach(function(v){
    h+='<line x1="'+X(v)+'" y1="'+(top-4)+'" x2="'+X(v)+'" y2="'+(top+rows.length*rowH)+'" class="grid"/>'+
       '<text x="'+X(v)+'" y="'+(top+rows.length*rowH+18)+'" class="axt">'+v+'</text>';
  });
  rows.forEach(function(r,i){
    var y0=top+i*rowH, y=y0+lab,bh=ph?14:18,cy=y+bh/2;
    var tip=r.project+', '+r.place+'. '+r.printer+'. '+r.units+' units. '+r.status+'.';
    h+=ph?'<text x="0" y="'+(y0+11)+'" class="rowl">'+esc(r.project)+'</text>'
         :'<text x="'+(L-10)+'" y="'+(cy+4)+'" class="rowl" text-anchor="end">'+esc(r.project)+'</text>';
    if(r.units>0) h+='<rect x="'+X(0)+'" y="'+y+'" width="'+(X(r.units)-X(0))+'" height="'+bh+'" class="bar clear"'+tipAttr(tip)+'/>';
    h+='<text x="'+(X(r.units)+8)+'" y="'+(cy+4)+'" class="val">'+r.units+' <tspan class="yr">'+esc(r.printer.split(',')[0])+'</tspan></text>';
  });
  h+='</svg>';
  var tbl='<table class="ftab"><thead><tr><th>Project</th><th>Place</th><th>Printer</th><th>Units</th><th>Status</th></tr></thead><tbody>'+
    rows.map(function(r){return '<tr><td>'+esc(r.project)+'</td><td>'+esc(r.place)+'</td><td>'+esc(r.printer)+'</td><td>'+r.units+'</td><td>'+esc(r.status)+'</td></tr>';}).join('')+'</tbody></table>';
  return figure('Printed housing projects in Texas, by units',
    (function(){var rx=new RegExp(PL.local||'Houston|San Leon'),hs=rows.filter(function(r){return rx.test(r.place);});
      return 'Printed, under way or committed. '+PL.name+': '+hs.length+' projects, '+
        hs.reduce(function(a,r){return a+r.units;},0)+' units.';})(),
    h, tbl);
}

/* 5. The field in time. Vertical, so a cluster of dates in one year can still
   carry a full label each: a label is pushed down until it clears the one
   above, and a leader line keeps it tied to its date. */
/* Build 67. The field in time. Years were drawn to scale, so 2017 to 2022 took
   half the figure with three events in it and 2024 to 2026 packed eleven into a
   third. Labels were pushed down to clear each other until they sat a year from
   their mark, the TODAY line ran through one of them, and four marks overlapped.
   It is now an ordered list, one row per event with its date beside it, so it
   cannot collide and it wraps on a phone instead of shrinking to 6px type. Time
   between rows still shows as extra space, capped. The list is its own table. */
function figTimeline(){
  var ev=(MK.timeline||[]).slice(); if(!ev.length) return '';
  var tv=function(e){return e.year+(e.month-1)/12;};
  ev.sort(function(a,b){return tv(a)-tv(b);});
  var lu=(D.last_updated||'').split('-'), today=lu.length>1?(+lu[0])+(+lu[1]-1)/12:null;
  var h='<ol class="tline" aria-label="Events, oldest first">', lastYear=null, prev=null, nowDone=false;
  ev.forEach(function(e){
    if(!nowDone&&today!==null&&tv(e)>today){
      h+='<li class="tnow" aria-label="Today"><span></span><span></span><span></span><span class="tnl">Today</span></li>';
      nowDone=true;
    }
    var gap=prev?Math.min(34,Math.max(0,(tv(e)-tv(prev))-0.25)*14):0;
    var when=e.when||(MONTHS[e.month-1]+' '+e.year);
    h+='<li'+(gap?' style="margin-top:'+Math.round(gap)+'px"':'')+'>'+
       '<span class="ty">'+(e.year!==lastYear?e.year:'')+'</span>'+
       '<span class="tm">'+esc(e.when?e.when.replace(/\s*\d{4}$/,''):MONTHS[e.month-1])+'</span>'+
       '<span class="tk '+e.kind+'" aria-hidden="true"></span>'+
       '<span class="tl-l"><span class="vh">'+esc(when)+': </span>'+esc(e.label)+'</span></li>';
    lastYear=e.year; prev=e;
  });
  h+='</ol>';
  var leg='<div class="flegend"><i><span class="dk in"></span>Entry or launch</i><i><span class="dk out"></span>Closure, sale or filing</i><i><span class="dk icon"></span>ICON</i></div>';
  return figure('Printer companies: entries and exits, '+ev[0].year+' to '+ev[ev.length-1].year, 'Entries, closures and ICON\u2019s own dates. Gaps between rows scale with time.', leg+h, '');
}
var MONTHS=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

/* Build 80. ICON's own test for opening a market, set against the volume this
   deck's builders publish for this market. The first line is ICON's, in
   BUILDER. The counts are the closings figures above, limited to figures that
   count this market alone. The printer count is arithmetic on the band's
   assumption of about 200 houses a year per Titan, which ICON has not
   published, and it says so. */
var TITAN_A_YEAR=200;
var ICON_MKT='https://www.builderonline.com/design/technology/icons-next-phase-building-a-scalable-platform-for-3d-printed-housing/';
function figThreshold(){
  var rows=(MK.closings||[]).filter(function(r){return !r.wide;});
  var band=rows.filter(function(r){return r.high>=25&&r.high<=400&&!r.over;});
  var mid=rows.filter(function(r){return (r.high>400||r.over)&&r.high<=1500;});
  var wideBand=(MK.closings||[]).filter(function(r){return r.wide&&r.high>=25&&r.high<=400&&!r.over;});
  var lo=band.reduce(function(a,r){return a+r.low;},0), hi=band.reduce(function(a,r){return a+r.high;},0);
  var mlo=mid.reduce(function(a,r){return a+r.low;},0), mhi=mid.reduce(function(a,r){return a+r.high;},0);
  function rng(a,b){return a===b?fmt(a):fmt(a)+' to '+fmt(b);}
  function ti(a,b){var x=Math.floor(a/TITAN_A_YEAR), y=Math.ceil(b/TITAN_A_YEAR);return x===y?String(x):x+' to '+y;}
  /* Build 83. One comparison, read across: each band's builders, their homes
     a year, and the Titans that volume would keep working, set against ICON's
     six to ten. It was five separate numbers in a row. */
  var wlo=wideBand.reduce(function(a,r){return a+r.low;},0), whi=wideBand.reduce(function(a,r){return a+r.high;},0);
  var rowsT=[['25 to 400 homes a year',band.length,band.length?rng(lo,hi):'0',band.length?ti(lo,hi):'0'],
             ['400 to 1,500 homes a year',mid.length,mid.length?rng(mlo,mhi):'0',mid.length?ti(mlo,mhi):'0']];
  /* A builder inside the band whose figure also counts other markets is shown
     on its own row and not turned into Titans: its local share is unknown. */
  if(wideBand.length) rowsT.splice(1,0,['25 to 400, a figure that also counts other markets',wideBand.length,rng(wlo,whi),'not counted']);
  var body='<table class="thtab"><thead><tr><th>Builders who publish homes closed a year</th><th class="num">Builders</th>'+
    '<th class="num">Homes a year</th><th class="num">Titans, at '+TITAN_A_YEAR+' a year</th></tr></thead><tbody>'+
    rowsT.map(function(r){return '<tr><td>'+esc(r[0])+'</td><td class="num">'+r[1]+'</td><td class="num">'+r[2]+'</td><td class="num">'+r[3]+'</td></tr>';}).join('')+
    '<tr class="test"><td>ICON\u2019s test for a full market opening</td><td></td><td></td><td class="num">6 to 10 printers</td></tr>'+
    '</tbody></table>';
  var tbl='<table class="ftab"><thead><tr><th>Builder</th><th class="num">Homes a year</th><th>Year</th><th>Band</th></tr></thead><tbody>'+
    band.concat(mid).map(function(r){return '<tr><td>'+esc(r.name)+'</td><td class="num">'+(r.over?'over ':'')+rng(r.low,r.high)+'</td><td>'+r.year+
      '</td><td>'+(r.high<=400&&!r.over?'25 to 400':'400 to 1,500')+'</td></tr>';}).join('')+'</tbody></table>';
  return figure('ICON’s six-to-ten printer test, against published volume',
    'ICON (BUILDER, 11 March 2026): demand for six to ten printers makes a market a candidate for a full opening. Target: small and mid-sized builders. '+
    'Titans: from '+PL.name+'-only figures, at an assumed '+TITAN_A_YEAR+' houses a year each. ICON\u2019s Titan page: a 2,500 square foot home in under seven days.',
    body, tbl, [{url:ICON_MKT,label:'BUILDER, 11 March 2026'},{url:'https://www.iconbuild.com/technology',label:'ICON\u2019s Titan page, September 2026'}], 'figThreshold');
}

/* Build 80. Dated news on the deck since 1 March 2026, newest first. Each row
   opens its firm. */
function figNews(){
  var rows=[];
  T.forEach(function(t){(t.news||[]).forEach(function(n){rows.push({t:t,n:n});});});
  if(!rows.length) return '';
  rows.sort(function(a,b){return a.n.date<b.n.date?1:a.n.date>b.n.date?-1:0;});
  var firms={}; rows.forEach(function(r){firms[r.t.target_id]=1;});
  var h='<ol class="nlist" aria-label="News, newest first">'+rows.map(function(r){
    return '<li><span class="nd">'+esc(r.n.date)+'</span>'+
      '<span class="nb"><button class="nf" data-id="'+r.t.target_id+'">'+esc(r.t.short||r.t.entity_name)+'</button>'+
      '<span class="nw">'+esc(r.n.what)+'</span>'+
      '<a class="src" href="'+esc(r.n.url)+'" target="_blank" rel="noopener">'+esc(r.n.outlet)+'</a></span></li>';}).join('')+'</ol>';
  return figure('News on this deck since 1 March 2026',
    rows.length+' items, '+Object.keys(firms).length+' firms. Land, communities, officers, capital.',
    h, '', null, 'figNews');
}

/* A segment opens the firms it counts. Each row opens the firm; the row's +
   adds it to the call list; the header offers the same set as a List filter. */
var SEG_OPEN=null;
function showSegment(key){
  var box=document.getElementById('segList'); if(!box) return;
  SEG_OPEN=key;
  var p=key.split(':'), g=p[0], m=p[1];
  var firms=T.filter(function(t){return t.group===g&&t.marks.innovation===m;});
  if(!firms.length){box.hidden=true;SEG_OPEN=null;return;}
  document.querySelectorAll('.fig .seg.on').forEach(function(e){e.classList.remove('on');});
  var seg=document.querySelector('.fig .seg[data-seg="'+key+'"]'); if(seg) seg.classList.add('on');
  var title=(GL[g]||g)+' · track record '+W[m]+' · '+firms.length+(firms.length===1?' firm':' firms');
  box.innerHTML='<div class="seghead"><b>'+esc(title)+'</b>'+
    '<span class="segact"><button class="fx" data-seglist="'+key+'">Open in List</button>'+
    '<button class="fx" id="segClose">Close</button></span></div>'+
    firms.map(function(t){
      var inCall=call.indexOf(t.target_id)>=0;
      var dec=t.decider_confirmed?'Decision-maker named':(t.decider_caveat?'Decision-maker to confirm':'');
      return '<div class="segrow"><button class="fbtn2 segname" data-id="'+t.target_id+'">'+esc(t.entity_name)+'</button>'+
        '<span class="segmeta">'+esc(t.region||'')+(dec?' · '+dec:'')+(t.key_stat?' · '+esc(t.key_stat):'')+'</span>'+
        '<button class="rowadd'+(inCall?' on':'')+'" data-add="'+t.target_id+'" aria-pressed="'+inCall+
        '" aria-label="'+(inCall?'Remove ':'Add ')+esc(t.entity_name)+' to call list">'+(inCall?'\u2713':'+')+'</button></div>';
    }).join('');
  box.hidden=false;
  box.scrollIntoView({block:'nearest',behavior:'smooth'});
}


/* ------------------------------------------------------------- permits
   A different quantity from everything above. Census counts units AUTHORISED
   BY PERMIT; the closings chart counts houses handed over by a builder. They
   are never added, divided or drawn on one axis. Magnitude here is grey to
   ink: the accent stays reserved for the third count. */
var PM=D.permits||{};
var PSRC=PM.sources||[];
/* Build 68. A market's sources can name the figures they serve ("use"); a
   market whose sources do not is matched on the URL, as Houston's are. */
function psrc(){var a=[].slice.call(arguments);
  if(PSRC.some(function(s){return s.use;})){
    var tags=a.filter(function(k){return k.charAt(0)==='#';}).map(function(k){return k.slice(1);});
    if(!tags.length) tags=[PUSE[a[0]]||a[0]];
    return PSRC.filter(function(s){return (s.use||[]).some(function(u){return tags.indexOf(u)>-1;});});}
  return PSRC.filter(function(s){return a.some(function(k){return k.charAt(0)!=='#'&&s.url.indexOf(k)>-1;});});}
var PUSE={huduser:'county',definitions:'metro'};
function nword(n){return ['no','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen'][n]||String(n);}
/* Build 67. Magnitude runs from the paper to the ink in either theme, so the
   dark theme has its own ramp, and the label on a cell is whichever of the two
   inks reads on it. */
var LRAMP=['#EDEDED','#D6D6D6','#B6B6B6','#8A8A8A','#4F4F4F','#111111'];
var DRAMP=['#1D1F23','#34363B','#50535A','#7C7F86','#B5B7BB','#ECECEC'];
function isDark(){return document.documentElement.getAttribute('data-theme')==='dark';}
function ramp(){return isDark()?DRAMP:LRAMP;}
function shade(v,max){ /* 0..1 -> paper to ink, five steps, printable */
  if(!max) return ramp()[0];
  var t=Math.sqrt(v/max), i=Math.min(5,Math.floor(t*5.999));
  return ramp()[i];
}
function inkOn(hex){
  var n=parseInt(hex.slice(1),16), r=(n>>16)&255, g=(n>>8)&255, b=n&255;
  return (0.2126*r+0.7152*g+0.0722*b)/255<0.45?'#FFFFFF':'#111111';
}

/* 7. The metro series. One column a year, single family only. */
function figPermits(){
  var rows=PM.msa||[]; if(!rows.length) return '';
  var ph=NARROW, PH_=ph?200:250, W=ph?CW:940,L=ph?46:58,R=ph?4:16,T=ph?14:30,B=ph?34:46,H=T+PH_+B;
  var max=Math.max.apply(null,rows.map(function(r){return r.sf;}));
  var bw=(W-L-R)/rows.length;
  var X=function(i){return L+i*bw;}, Y=function(v){return T+PH_-PH_*v/max;};
  var h=svgOpen(W,H);
  (ph?[0,25000,50000]:[0,10000,20000,30000,40000,50000]).filter(function(v){return v<=max*1.02||v===0;}).forEach(function(v){
    h+='<line x1="'+L+'" y1="'+Y(v)+'" x2="'+(W-R)+'" y2="'+Y(v)+'" class="grid"/>'+
       '<text x="'+(L-8)+'" y="'+(Y(v)+4)+'" class="axe">'+fmt(v)+'</text>';
  });
  rows.forEach(function(r,i){
    var tip=r.year+': '+fmt(r.sf)+' single-family units authorized, '+fmt(r.all)+' units of all types.';
    h+='<rect x="'+(X(i)+(ph?.5:1))+'" y="'+Y(r.sf)+'" width="'+(bw-(ph?1:2))+'" height="'+(T+PH_-Y(r.sf))+
       '" class="bar"'+tipAttr(tip)+'/>';
    if(r.year%(ph?10:5)===0)
      h+='<text x="'+(X(i)+bw/2)+'" y="'+(T+PH_+16)+'" class="axt">'+r.year+'</text>';
  });
  h+='<line x1="'+L+'" y1="'+(T+PH_)+'" x2="'+(W-R)+'" y2="'+(T+PH_)+'" class="axis"/></svg>';
  var tbl='<table class="ftab"><thead><tr><th>Year</th><th>Single family</th><th>All units</th></tr></thead><tbody>'+
    rows.slice().reverse().map(function(r){return '<tr><td>'+r.year+'</td><td>'+fmt(r.sf)+'</td><td>'+fmt(r.all)+'</td></tr>';}).join('')+
    '</tbody></table>';
  var g=PM.geo||{};
  return figure('Single-family units authorized, '+(g.name||''),
    'Permits across '+nword((PM.counties||[]).length)+' counties, '+rows[0].year+' to '+rows[rows.length-1].year+
    '. A permit is not a closing. Townhouses count as single family.',
    h, tbl, PSRC.some(function(s){return s.use;})?PSRC.filter(function(s){return (s.use||[]).indexOf('metro')>-1;}):psrc('huduser','definitions'));
}

/* 8. The ten counties, drawn. Outlines are TxDOT's, at a fidelity where a shared
   border between two counties lands on the same pixel, so the seam reads as one
   line. Fill is the sequential ramp; labels sit at each county's pole of
   inaccessibility rather than its centroid, so they stay inside the shape. */
var PYEAR=2025;
function figCountyMap(){
  var G=PM.geom||[], C=PM.counties||[]; if(!G.length||!C.length) return '';
  var yrs=C[0].years, W=NARROW?CW:680,H=NARROW?Math.round(CW*470/680)+34:470, PAD=NARROW?10:26;
  var lo=[999,999],hi=[-999,-999];
  G.forEach(function(f){f.rings.forEach(function(p){p.forEach(function(r){r.forEach(function(c){
    lo[0]=Math.min(lo[0],c[0]);lo[1]=Math.min(lo[1],c[1]);
    hi[0]=Math.max(hi[0],c[0]);hi[1]=Math.max(hi[1],c[1]);});});});});
  var k=Math.cos((lo[1]+hi[1])/2*Math.PI/180);
  var sc=Math.min((W-2*PAD)/((hi[0]-lo[0])*k), (H-2*PAD-30)/(hi[1]-lo[1]));
  var ox=(W-(hi[0]-lo[0])*k*sc)/2, oy=PAD;
  var PX=function(c){return [ox+(c[0]-lo[0])*k*sc, oy+(hi[1]-c[1])*sc];};

  /* the point inside a ring that is farthest from any edge: a coarse grid pass
     then two refinements. Cheap, and it never puts a label outside its county. */
  function ptSeg(px,py,ax,ay,bx,by){
    var dx=bx-ax, dy=by-ay, l=dx*dx+dy*dy, t=l?((px-ax)*dx+(py-ay)*dy)/l:0;
    t=t<0?0:(t>1?1:t);
    var qx=ax+t*dx-px, qy=ay+t*dy-py; return Math.sqrt(qx*qx+qy*qy);
  }
  function inside(px,py,r){
    var on=false;
    for(var i=0,j=r.length-1;i<r.length;j=i++){
      var a=r[i],b=r[j];
      if((a[1]>py)!==(b[1]>py) && px<(b[0]-a[0])*(py-a[1])/(b[1]-a[1])+a[0]) on=!on;
    }
    return on;
  }
  /* Build 70. A lake is a hole: the label sits on land, clear of the shore. */
  function labelPoint(r,holes){
    var x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;
    r.forEach(function(p){x0=Math.min(x0,p[0]);y0=Math.min(y0,p[1]);x1=Math.max(x1,p[0]);y1=Math.max(y1,p[1]);});
    holes=(holes||[]).filter(function(h){return h.some(function(p){return p[0]>=x0&&p[0]<=x1&&p[1]>=y0&&p[1]<=y1;});});
    var edges=[r].concat(holes);
    var best=null, bd=-1, step=Math.max((x1-x0),(y1-y0))/22;
    function scan(cx0,cy0,cx1,cy1,st){
      for(var x=cx0;x<=cx1;x+=st) for(var y=cy0;y<=cy1;y+=st){
        if(!inside(x,y,r)) continue;
        if(holes.some(function(h){return inside(x,y,h);})) continue;
        var d=1e9;
        for(var e=0;e<edges.length&&d>bd;e++){
          var q=edges[e];
          for(var i=0,j=q.length-1;i<q.length;j=i++){
            d=Math.min(d,ptSeg(x,y,q[i][0],q[i][1],q[j][0],q[j][1]));
            if(d<bd) break;
          }
        }
        if(d>bd){bd=d;best=[x,y];}
      }
    }
    scan(x0,y0,x1,y1,step);
    if(best){ scan(best[0]-step,best[1]-step,best[0]+step,best[1]+step,step/4); }
    if(best){ scan(best[0]-step/4,best[1]-step/4,best[0]+step/4,best[1]+step/4,step/12); }
    return {p:best||[(x0+x1)/2,(y0+y1)/2], r:bd};
  }
  /* placed once, in screen space, and cached: the projection never changes */
  var WAT=PM.water||[];
  var LAKES=[]; WAT.forEach(function(w){w.rings.forEach(function(p){LAKES.push(p[0].map(PX));});});
  var ANCHOR={};
  G.forEach(function(f){
    var big=null, ba=-1;
    f.rings.forEach(function(poly){
      var r=poly[0], a=0;
      for(var j=0;j<r.length;j++){var q=r[j],w=r[(j+1)%r.length];a+=q[0]*w[1]-w[0]*q[1];}
      a=Math.abs(a/2); if(a>ba){ba=a;big=r;}
    });
    ANCHOR[f.fips]=labelPoint(big.map(PX),LAKES);
  });

  var body='<div class="yrctl"><label for="pyr">Year</label>'+
    '<input type="range" id="pyr" min="'+yrs[0]+'" max="'+yrs[yrs.length-1]+'" value="'+PYEAR+'" step="1">'+
    '<output id="pyrv">'+PYEAR+'</output></div><div id="mapHost"></div>';
  var shown=yrs.filter(function(y,i){return y%5===0||i===yrs.length-1;});
  var tbl='<table class="ftab"><thead><tr><th>County</th>'+shown.map(function(y){return '<th class="num">'+y+'</th>';}).join('')+'</tr></thead><tbody>'+
    C.slice().sort(function(a,b){return b.sf[b.sf.length-1]-a.sf[a.sf.length-1];}).map(function(c){
      return '<tr><td>'+esc(c.name)+'</td>'+shown.map(function(y){
        return '<td class="num">'+fmt(c.sf[c.years.indexOf(y)])+'</td>';}).join('')+'</tr>';}).join('')+
    '</tbody></table>';

  window.__drawMap=function(){
    var i=yrs.indexOf(PYEAR); if(i<0) i=yrs.length-1;
    var max=Math.max.apply(null,C.map(function(c){return c.sf[i];}));
    var h=svgOpen(W,H,'map');
    var D_={};
    G.forEach(function(f){
      D_[f.fips]=f.rings.map(function(poly){return poly.map(function(ring){
        return 'M'+ring.map(function(pt){var q=PX(pt);return q[0].toFixed(1)+' '+q[1].toFixed(1);}).join('L')+'Z';}).join('');}).join('');
    });
    h+='<g class="ctys">';
    G.forEach(function(f){
      var c=C.filter(function(x){return x.fips===f.fips;})[0]; if(!c) return;
      var v=c.sf[i], fill=shade(v,max);
      h+='<path d="'+D_[f.fips]+'" class="cty" fill="'+fill+'"'+
         tipAttr(c.name+' County, '+PYEAR+': '+fmt(v)+' single-family units authorized')+'/>';
    });
    h+='</g>';
    /* lakes, clipped to the metro so a reservoir on the edge stops at the county line */
    if(WAT.length){
      h+='<clipPath id="mapClip">'+G.map(function(f){return '<path d="'+D_[f.fips]+'"/>';}).join('')+'</clipPath>'+
         '<g class="water" clip-path="url(#mapClip)">'+WAT.map(function(w){
           return '<path fill-rule="evenodd" d="'+w.rings.map(function(poly){return poly.map(function(ring){
             return 'M'+ring.map(function(pt){var q=PX(pt);return q[0].toFixed(1)+' '+q[1].toFixed(1);}).join('L')+'Z';}).join('');}).join('')+
             '"><title>'+esc(w.name)+'</title></path>';}).join('')+'</g>';
    }
    h+='<g class="ctyedge">'+G.map(function(f){return '<path d="'+D_[f.fips]+'"/>';}).join('')+
       '</g><g class="ctyls">';
    G.forEach(function(f){
      var c=C.filter(function(x){return x.fips===f.fips;})[0]; if(!c) return;
      var v=c.sf[i], fill=shade(v,max), A=ANCHOR[f.fips], x=A.p[0], y=A.p[1];
      var tight=A.r<30, fs=tight?10:12, vs=tight?9:10.5;
      var pen=' fill="'+inkOn(fill)+'" stroke="'+fill+'" stroke-width="'+(tight?2.4:3)+'"';
      /* On a phone the map is half the size, so a county too small to hold its
         name carries none; its figure is in the tooltip and the table. */
      if(NARROW){ if(A.r<10) return; tight=A.r<20; fs=tight?10.5:12; vs=10;
        pen=' fill="'+inkOn(fill)+'" stroke="'+fill+'" stroke-width="2.4"';
        h+='<text x="'+x.toFixed(0)+'" y="'+(y+(tight?4:-2)).toFixed(0)+'" class="ctyl" style="font-size:'+fs+'px"'+pen+'>'+esc(c.name)+'</text>'+
           (tight?'':'<text x="'+x.toFixed(0)+'" y="'+(y+11).toFixed(0)+'" class="ctyv" style="font-size:'+vs+'px"'+pen+'>'+fmt(v)+'</text>');
        return; }
      h+='<text x="'+x.toFixed(0)+'" y="'+(y-2).toFixed(0)+'" class="ctyl" style="font-size:'+fs+'px"'+pen+'>'+esc(c.name)+'</text>'+
         '<text x="'+x.toFixed(0)+'" y="'+(y+(tight?9:12)).toFixed(0)+'" class="ctyv" style="font-size:'+vs+'px"'+pen+'>'+fmt(v)+'</text>';
    });
    h+='</g>';
    /* key: a continuous strip, two labels, no ladder of numbers */
    var KW=NARROW?140:170, kx=NARROW?0:14, ky=H-34;
    h+='<text x="'+kx+'" y="'+(ky-9)+'" class="axl">Units authorized, '+PYEAR+'</text>';
    ramp().forEach(function(fill,b){
      h+='<rect x="'+(kx+b*(KW/6)).toFixed(1)+'" y="'+ky+'" width="'+(KW/6).toFixed(1)+'" height="9" fill="'+fill+'" '+
         'style="stroke:var(--rule2)" stroke-width=".5"/>';
    });
    h+='<text x="'+kx+'" y="'+(ky+20)+'" class="axs">0</text>'+
       '<text x="'+(kx+KW)+'" y="'+(ky+20)+'" class="axe">'+fmt(max)+'</text>';
    h+='</svg>';
    var host=document.getElementById('mapHost'); if(host) host.innerHTML=h;
  };
  return figure('Single-family permits by county',
    'Square-root scale. Outlines'+(WAT.length?' and lakes':'')+': '+(PL.outline||'TxDOT')+'. Drag the year.'+
    (NARROW?' Unlabelled counties are in the table.':''),
    body, tbl, psrc('huduser','txdot','#county','#map'), 'figMap');
}

/* 9. The same ten counties as a matrix, which is where the movement shows. */
var PMODE='shr';
function figCountyMatrix(){
  var C=PM.counties||[], M=PM.msa||[]; if(!C.length) return '';
  var yrs=C[0].years;
  var body='<div class="mtxctl"><div class="seg" role="group">'+
    '<button type="button" data-pmode="shr" aria-pressed="'+(PMODE==='shr')+'">Share of metro</button>'+
    '<button type="button" data-pmode="own" aria-pressed="'+(PMODE==='own')+'">Against its own peak</button>'+
    '</div></div><div id="mtxHost"></div>';
  var tbl='<table class="ftab"><thead><tr><th>County</th>'+yrs.map(function(y){return '<th>'+y+'</th>';}).join('')+'</tr></thead><tbody>'+
    C.slice().sort(function(a,b){return b.sf[b.sf.length-1]-a.sf[a.sf.length-1];}).map(function(c){
      return '<tr><td>'+esc(c.name)+'</td>'+c.sf.map(function(v){return '<td>'+fmt(v)+'</td>';}).join('')+'</tr>';}).join('')+
    '</tbody></table>';
  window.__drawMtx=function(){
    var rows=C.slice().sort(function(a,b){return b.sf[b.sf.length-1]-a.sf[a.sf.length-1];});
    var mi={}; (M||[]).forEach(function(m){mi[m.year]=m.sf;});
    var L=NARROW?88:170, cw=NARROW?(CW-L-4)/yrs.length:Math.max(26,Math.min(34,(900-170)/yrs.length)), rh=NARROW?24:30, T=26;
    var W=L+cw*yrs.length+10, H=T+rh*rows.length+34;
    var max=0, peak={};
    rows.forEach(function(c){
      peak[c.fips]=Math.max.apply(null,c.sf);
      c.sf.forEach(function(v,i){
        var t=(PMODE==='shr')?(mi[yrs[i]]?v/mi[yrs[i]]:0):(peak[c.fips]?v/peak[c.fips]:0);
        if(t>max) max=t;});});
    var h=svgOpen(W,H,'mtx');
    yrs.forEach(function(y,i){ if(y%5===0||i===yrs.length-1)
      h+='<text x="'+(L+i*cw+cw/2)+'" y="'+(T-8)+'" class="axt">'+String(y).slice(2)+'</text>';});
    rows.forEach(function(c,r){
      h+='<text x="'+(L-(NARROW?8:10))+'" y="'+(T+r*rh+rh/2+4)+'" class="rowl'+(NARROW?' sm':'')+'" text-anchor="end">'+esc(c.name)+'</text>';
      c.sf.forEach(function(v,i){
        var m=mi[yrs[i]];
        var val=(PMODE==='shr')?(m?v/m:0):(peak[c.fips]?v/peak[c.fips]:0);
        var fill=shade(val,max);
        var tip=c.name+' County, '+yrs[i]+': '+fmt(v)+' single-family units authorized'+
          (m?', '+(100*v/m).toFixed(1)+' per cent of the metro':'')+'.';
        h+='<rect x="'+(L+i*cw)+'" y="'+(T+r*rh)+'" width="'+(cw-(NARROW?1:2))+'" height="'+(rh-2)+
           '" fill="'+fill+'" class="cell"'+tipAttr(tip)+'/>';
      });
    });
    h+='</svg>';
    var host=document.getElementById('mtxHost'); if(host) host.innerHTML=h;
  };
  return figure('Single-family permits by county and year',
    yrs[0]+' to '+yrs[yrs.length-1]+'. Share of metro: each county against the metro that year. Own peak: each county against its busiest year.',
    body, tbl, psrc('huduser'));
}

/* 10. Permit-issuing jurisdictions. */
var JYEAR=null;
function figPlaces(){
  var P=PM.places||[], yrs=PM.place_years||[]; if(!P.length) return '';
  if(JYEAR===null) JYEAR=yrs[yrs.length-1];
  var body='<div class="mtxctl"><div class="seg" role="group">'+
    yrs.map(function(y){return '<button type="button" data-jyr="'+y+'" aria-pressed="'+(y===JYEAR)+'">'+y+'</button>';}).join('')+
    '</div></div><div id="jurHost"></div>';
  var li=yrs.length-1;
  var tbl='<table class="ftab"><thead><tr><th>Jurisdiction</th><th>County</th>'+yrs.map(function(y){return '<th>'+y+'</th>';}).join('')+'</tr></thead><tbody>'+
    P.slice().sort(function(a,b){return b.sf[li]-a.sf[li];}).map(function(p){
      return '<tr><td>'+esc(p.name)+'</td><td>'+esc(p.county)+'</td>'+p.sf.map(function(v){return '<td>'+fmt(v)+'</td>';}).join('')+'</tr>';}).join('')+
    '</tbody></table>';
  window.__drawJur=function(){
    var i=yrs.indexOf(JYEAR); if(i<0) i=yrs.length-1;
    var rows=P.slice().sort(function(a,b){return b.sf[i]-a.sf[i];}).slice(0,25);
    var ph=NARROW, W=ph?CW:900,L=ph?0:260,R=ph?52:90,rowH=ph?34:24,T=ph?4:14,lab=ph?15:0,H=T+rows.length*rowH+18;
    var max=Math.max.apply(null,rows.map(function(r){return r.sf[i];}));
    var X=function(v){return L+(W-L-R)*v/max;};
    var h=svgOpen(W,H);
    rows.forEach(function(p,r){
      var y=T+r*rowH+lab, tip=p.name+', '+p.county+' County, '+JYEAR+': '+fmt(p.sf[i])+' single-family units authorized.';
      h+=(ph?'<text x="0" y="'+(y-3)+'" class="rowl sm">'+esc(p.name)+'</text>'
            :'<text x="'+(L-10)+'" y="'+(y+14)+'" class="rowl sm" text-anchor="end">'+esc(p.name)+'</text>')+
         '<rect x="'+L+'" y="'+(y+3)+'" width="'+(X(p.sf[i])-L)+'" height="'+(rowH-9-(ph?lab-3:0))+'" class="bar'+
         (/Unincorporated/i.test(p.name)?' uninc':'')+'"'+tipAttr(tip)+'/>'+
         '<text x="'+(X(p.sf[i])+8)+'" y="'+(y+14)+'" class="val">'+fmt(p.sf[i])+'</text>';
    });
    h+='</svg>';
    var host=document.getElementById('jurHost'); if(host) host.innerHTML=h;
  };
  return figure('Single-family permits by issuing jurisdiction',
    (function(){var i=yrs.length-1,a=0,c=0;P.forEach(function(p){a+=p.sf[i]||0;});
      (PM.counties||[]).forEach(function(k){var j=k.years.indexOf(yrs[i]);c+=j>-1?k.sf[j]:0;});
      return Math.abs(a-c)<=Math.max(5,c*0.001)?P.length+' jurisdictions. They sum to the '+nword((PM.counties||[]).length)+' counties exactly.':
        P.length+' jurisdictions, '+Math.round(100*a/c)+' percent of '+yrs[i]+' metro units.';})()+' Top 25 drawn. Outlined: unincorporated county. Solid: a city. '+(function(){var i=yrs.length-1,u=0,a=0;
      P.forEach(function(p){a+=p.sf[i]||0; if(/Unincorporated/i.test(p.name)) u+=p.sf[i]||0;});
      return a?yrs[i]+': '+fmt(u)+' of '+fmt(a)+' units, '+Math.round(100*u/a)+' percent, permitted by a county.':'';})(),
    body, tbl, psrc('huduser','#place'));
}

function figure(title,caption,body,table,sources,id,extra){
  var src=(sources||[]).map(function(s){
    return '<a class="src" href="'+esc(s.url)+'" target="_blank" rel="noopener">'+esc(s.label)+'</a>';}).join('');
  return '<section class="figs"'+(id?' id="'+id+'"':'')+'><h3>'+esc(title)+'</h3>'+
    '<p class="fcap">'+esc(caption)+'</p>'+
    '<div class="fwrap">'+body+'</div>'+
    (src?'<p class="figsrc"><span class="lab">Source</span>'+src+'</p>':'')+
    (extra||'')+
    (table?'<details class="ftable"><summary>As a table</summary>'+table+'</details>':'')+'</section>';
}

function drawMarket(){
  sizeCharts();
  var _mt=document.getElementById('mkTitle'); if(_mt) _mt.textContent=PL.name+' in figures';
  /* Build 82. The view is one argument in five steps: how many homes get
     permitted here, who builds them, which of those builders fit one or two
     printers, who prints here already, and what changed this year. The strip
     at the top carries one number per step, in the same order, and each opens
     its step. */
  var ms=PM.msa||[], last=ms.length?ms[ms.length-1]:null;
  var cl=MK.closings||[], local=cl.filter(function(r){return !r.wide;});
  var band=local.filter(function(r){return r.high>=25&&r.high<=400&&!r.over;});
  var rx=new RegExp(PL.local||'Houston|San Leon');
  var printed=(MK.printed||[]).filter(function(r){return rx.test(r.place);});
  var pu=printed.reduce(function(a,r){return a+r.units;},0);
  var nn=0; T.forEach(function(t){nn+=(t.news||[]).length;});
  var steps=[
    ['mkDemand','Homes permitted',last?fmt(last.sf):'0',
      last?'single-family units permitted in '+last.year+', whole metro':'no permit series'],
    ['mkBuyers','Who builds them',cl.length+' of '+NB,'builders and developers publish homes closed a year'],
    ['mkFit','Fit for one or two printers',String(band.length),
      (band.length===1?'builder publishes ':'builders publish ')+PL.name+' volume inside the band one or two printers would cover'],
    ['mkPrint','Printing in Texas',fmt(pu),'printed homes in '+PL.name+', built, under way or committed'],
    ['mkNews','News since 1 March 2026',String(nn),'dated items on firms on this deck']];
  document.getElementById('mkStats').innerHTML=steps.map(function(s,i){
    return '<button class="stat" type="button" data-goto="'+s[0]+'"><b>'+s[2]+'</b><span>'+(i+1)+' \u00b7 '+esc(s[3])+'</span></button>';}).join('');
  function sec(i,body){var s=steps[i];
    return '<div class="mksec" id="'+s[0]+'"><div class="mksech"><span class="mkn">'+(i+1)+'</span><h3>'+esc(s[1])+'</h3></div>'+body+'</div>';}
  document.getElementById('mkBody').innerHTML=
    sec(0,figPermits()+figCountyMap()+figCountyMatrix()+figPlaces())+
    sec(1,figClosings()+figOwners())+
    sec(2,figThreshold()+figSections())+
    sec(3,figPrinted()+figTimeline())+
    sec(4,figNews());
  if(window.__drawMap) window.__drawMap();
  if(window.__drawMtx) window.__drawMtx();
  if(window.__drawJur) window.__drawJur();
  var yr=document.getElementById('pyr');
  if(yr) yr.addEventListener('input',function(){
    PYEAR=+yr.value; var o=document.getElementById('pyrv'); if(o) o.textContent=PYEAR;
    window.__drawMap();});
  document.querySelectorAll('[data-pmode]').forEach(function(b){
    b.addEventListener('click',function(){
      PMODE=b.getAttribute('data-pmode');
      document.querySelectorAll('[data-pmode]').forEach(function(x){
        x.setAttribute('aria-pressed', String(x.getAttribute('data-pmode')===PMODE));});
      window.__drawMtx();});});
  document.querySelectorAll('[data-jyr]').forEach(function(b){
    b.addEventListener('click',function(){
      JYEAR=+b.getAttribute('data-jyr');
      document.querySelectorAll('[data-jyr]').forEach(function(x){
        x.setAttribute('aria-pressed', String(+x.getAttribute('data-jyr')===JYEAR));});
      window.__drawJur();});});
  if(SEG_OPEN) showSegment(SEG_OPEN);
}

/* one tooltip for every mark */
(function(){
  var tip=document.createElement('div');tip.id='tip';tip.setAttribute('role','tooltip');tip.hidden=true;
  document.body.appendChild(tip);
  var touched=0;
  function show(e){if(Date.now()-touched<900) return;
    var el=e.target.closest&&e.target.closest('[data-tip]'); if(!el){tip.hidden=true;return;}
    tip.textContent=el.getAttribute('data-tip');tip.hidden=false;move(e);}
  function move(e){if(Date.now()-touched<900) return;
    var x=e.clientX+14,y=e.clientY+14;
    var r=tip.getBoundingClientRect();
    if(x+r.width>window.innerWidth-12) x=e.clientX-r.width-14;
    if(y+r.height>window.innerHeight-12) y=e.clientY-r.height-14;
    tip.style.left=Math.max(12,x)+'px';tip.style.top=y+'px';}
  /* Build 78. A tap on a mark shows its tip above the finger, centred and kept
     on screen; a tap anywhere else, or a scroll, puts it away. */
  document.addEventListener('pointerdown',function(e){
    if(e.pointerType!=='touch') return; touched=Date.now();
    var el=e.target.closest&&e.target.closest('[data-tip]'); if(!el){tip.hidden=true;return;}
    tip.textContent=el.getAttribute('data-tip');tip.hidden=false;
    var r=tip.getBoundingClientRect();
    var x=Math.min(Math.max(12,e.clientX-r.width/2),window.innerWidth-r.width-12);
    var y=e.clientY-r.height-22; if(y<70) y=e.clientY+28;
    tip.style.left=x+'px';tip.style.top=y+'px';});
  window.addEventListener('scroll',function(){if(!touched||Date.now()-touched<400) return; tip.hidden=true;},{passive:true});
  document.addEventListener('mouseover',show);
  document.addEventListener('mousemove',function(e){if(!tip.hidden)move(e);});
  document.addEventListener('mouseout',function(e){if(Date.now()-touched<900) return;
    if(e.target.closest&&e.target.closest('[data-tip]'))tip.hidden=true;});
})();
