/* ------------------------------------------------------------------ market
   Six figures drawn from the same records the other views read. Every chart
   is a plain SVG built here: one hue for magnitude (ink, with grey for a
   Partly), the accent only where it already means the third count, a table
   under each chart, and a tooltip on every mark. Nothing is estimated; a firm
   with no published figure is absent and the caption says how many that is. */
var MK=D.market||{};
function fmt(n){return String(n).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
function svgOpen(w,h,cls){return '<svg class="fig'+(cls?' '+cls:'')+'" viewBox="0 0 '+w+' '+h+
  '" width="100%" preserveAspectRatio="xMinYMin meet" role="img" aria-hidden="false">';}
function tipAttr(t){return ' data-tip="'+esc(t)+'"';}

/* 1. Published annual closings, one bar per firm, with the machine-fit bands. */
function figClosings(){
  var rows=MK.closings||[]; if(!rows.length) return '';
  var W=900,L=190,R=110,rowH=30,top=34,H=top+rows.length*rowH+30;
  var max=1200, X=function(v){return L+(W-L-R)*Math.min(v,max)/max;};
  var h=svgOpen(W,H);
  // bands
  (MK.bands||[]).forEach(function(b,i){
    var x0=X(b[0]),x1=X(Math.min(b[1],max));
    h+='<rect x="'+x0+'" y="'+(top-8)+'" width="'+(x1-x0)+'" height="'+(rows.length*rowH+8)+
       '" class="band b'+i+'"/>';
    h+='<text x="'+(x0+6)+'" y="'+(top-14)+'" class="axl">'+esc(b[2])+
       (b[1]>max?', to '+fmt(b[1]):'')+'</text>';
  });
  // gridlines
  [0,200,400,600,800,1000,1200].forEach(function(v){
    h+='<line x1="'+X(v)+'" y1="'+(top-8)+'" x2="'+X(v)+'" y2="'+(top+rows.length*rowH)+'" class="grid"/>'+
       '<text x="'+X(v)+'" y="'+(top+rows.length*rowH+18)+'" class="axt">'+fmt(v)+'</text>';
  });
  rows.forEach(function(r,i){
    var y=top+i*rowH, bh=18, cy=y+bh/2;
    var tip=r.name+': '+(r.low===r.high?fmt(r.high):fmt(r.low)+' to '+fmt(r.high))+
            ' homes, '+r.year+'. '+r.source+'. Printer fit '+W_[r.fit]+'.';
    h+='<text x="'+(L-10)+'" y="'+(cy+4)+'" class="rowl" text-anchor="end" data-id="'+r.id+'">'+esc(r.short)+'</text>';
    h+='<rect x="'+X(0)+'" y="'+y+'" width="'+(X(r.low)-X(0))+'" height="'+bh+'" rx="0" class="bar '+r.fit+'"'+tipAttr(tip)+'/>';
    if(r.high>r.low){
      h+='<line x1="'+X(r.low)+'" y1="'+cy+'" x2="'+X(r.high)+'" y2="'+cy+'" class="range"'+tipAttr(tip)+'/>'+
         '<line x1="'+X(r.high)+'" y1="'+(cy-5)+'" x2="'+X(r.high)+'" y2="'+(cy+5)+'" class="range"/>';
    }
    h+='<text x="'+(X(r.high)+8)+'" y="'+(cy+4)+'" class="val">'+
       (r.low===r.high?fmt(r.high):fmt(r.low)+'–'+fmt(r.high))+' <tspan class="yr">'+r.year+'</tspan></text>';
  });
  h+='</svg>';
  var tbl='<table class="ftab"><thead><tr><th>Firm</th><th>Homes a year</th><th>Year</th><th>Printer fit</th><th>Source</th></tr></thead><tbody>'+
    rows.map(function(r){return '<tr><td>'+esc(r.name)+'</td><td>'+(r.low===r.high?fmt(r.high):fmt(r.low)+' to '+fmt(r.high))+
      '</td><td>'+r.year+'</td><td>'+W_[r.fit]+'</td><td>'+esc(r.source)+'</td></tr>';}).join('')+'</tbody></table>';
  return figure('Published annual closings',
    rows.length+' of '+T.length+' firms publish an annual figure. The other '+MK.closings_missing+
    ' do not, and are not drawn. Solid bars are a Yes on Printer fit; grey bars are a Partly. A range is drawn to its low end with a line to its high end. The shaded bands are an assumption; how they were set is under How each number is produced, below.',
    h, tbl);
}

/* 2. Track record and named decision-makers, by section. */
function figSections(){
  var rows=MK.by_section||[]; if(!rows.length) return '';
  var W=900,L=230,R=40,rowH=34,top=30,H=top+rows.length*rowH+12;
  var max=Math.max.apply(null,rows.map(function(r){return r.n;}));
  var X=function(v){return (W-L-R)*v/max;};
  var h=svgOpen(W,H);
  rows.forEach(function(r,i){
    var y=top+i*rowH,bh=20,x=L;
    h+='<text x="'+(L-10)+'" y="'+(y+14)+'" class="rowl" text-anchor="end">'+esc(r.label)+'</text>';
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
    'Each bar is one section, one segment per verdict. Click a segment for the firms in it. The table under it adds the named decision-maker count and how many firms in each section carry at least one link.',
    leg+h+'<div class="seglist" id="segList" hidden></div>', tbl);
}

/* 3. Land owners and the builders inside their communities. */
function figOwners(){
  var owners=(MK.owners||[]).filter(function(o){return o.builders.length;});
  if(!owners.length) return '';
  var names=[];owners.forEach(function(o){o.builders.forEach(function(b){if(names.indexOf(b.name)<0)names.push(b.name);});});
  var W=900,L=40,R=40,colL=230,colR=W-260,rowH=30,top=24;
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
    var off=false; owners.forEach(function(o){o.builders.forEach(function(b){if(b.name===nm&&b.off)off=true;});});
    h+='<text x="'+colR+'" y="'+(yb(j)+14)+'" class="node'+(id?'':' off')+'"'+(id?' data-id="'+id+'"':'')+'>'+esc(nm)+
       (id?'':' <tspan class="cnt">'+(off?'held off the deck':'not screened')+'</tspan>')+'</text>';
  });
  h+='</svg>';
  var tbl='<table class="ftab"><thead><tr><th>Land owner</th><th>Communities</th><th>Builders inside, on this screen</th></tr></thead><tbody>'+
    (MK.owners||[]).map(function(o){return '<tr><td>'+esc(o.short)+'</td><td>'+esc(o.line)+'</td><td>'+
      (o.builders.length?o.builders.map(function(b){return esc(b.name);}).join(', '):'none on this screen')+'</td></tr>';}).join('')+'</tbody></table>';
  return figure('Land owners and the builders inside their communities',
    'Left, the masterplan owners screened here; right, the builders each one lists in its communities. A name opens the firm. Howard Hughes lists none of the builders screened.',
    h, tbl);
}

/* 4. Printed homes in Texas, on the public record. */
function figPrinted(){
  var rows=MK.printed||[]; if(!rows.length) return '';
  var W=900,L=230,R=150,rowH=30,top=12,H=top+rows.length*rowH+30;
  var max=Math.max.apply(null,rows.map(function(r){return r.units;}))||1;
  var X=function(v){return L+(W-L-R)*v/max;};
  var h=svgOpen(W,H);
  [0,25,50,75,100].forEach(function(v){
    h+='<line x1="'+X(v)+'" y1="'+(top-4)+'" x2="'+X(v)+'" y2="'+(top+rows.length*rowH)+'" class="grid"/>'+
       '<text x="'+X(v)+'" y="'+(top+rows.length*rowH+18)+'" class="axt">'+v+'</text>';
  });
  rows.forEach(function(r,i){
    var y=top+i*rowH,bh=18,cy=y+bh/2;
    var tip=r.project+', '+r.place+'. '+r.printer+'. '+r.units+' units. '+r.status+'.';
    h+='<text x="'+(L-10)+'" y="'+(cy+4)+'" class="rowl" text-anchor="end">'+esc(r.project)+'</text>';
    if(r.units>0) h+='<rect x="'+X(0)+'" y="'+y+'" width="'+(X(r.units)-X(0))+'" height="'+bh+'" class="bar clear"'+tipAttr(tip)+'/>';
    h+='<text x="'+(X(r.units)+8)+'" y="'+(cy+4)+'" class="val">'+r.units+' <tspan class="yr">'+esc(r.printer.split(',')[0])+'</tspan></text>';
  });
  h+='</svg>';
  var tbl='<table class="ftab"><thead><tr><th>Project</th><th>Place</th><th>Printer</th><th>Units</th><th>Status</th></tr></thead><tbody>'+
    rows.map(function(r){return '<tr><td>'+esc(r.project)+'</td><td>'+esc(r.place)+'</td><td>'+esc(r.printer)+'</td><td>'+r.units+'</td><td>'+esc(r.status)+'</td></tr>';}).join('')+'</tbody></table>';
  return figure('Printed homes in Texas on the public record',
    (function(){var hs=rows.filter(function(r){return /Houston|San Leon/.test(r.place);});
      return 'Units printed, under way or committed, by project, with the printer. The '+hs.length+
        ' Greater Houston projects total '+hs.reduce(function(a,r){return a+r.units;},0)+' units.';})(),
    h, tbl);
}

/* 5. The field in time. Vertical, so a cluster of dates in one year can still
   carry a full label each: a label is pushed down until it clears the one
   above, and a leader line keeps it tied to its date. */
function figTimeline(){
  var ev=(MK.timeline||[]).slice(); if(!ev.length) return '';
  var W=700,top=20,bottom=24,axisX=64,minGap=24,dotX=64+18;
  var t0=2017,t1=2027.25,span=t1-t0,pxPerYear=66;
  var H=top+bottom+span*pxPerYear;
  var Y=function(y,m){return top+(y+(m-1)/12-t0)*pxPerYear;};
  ev.sort(function(a,b){return (a.year+(a.month-1)/12)-(b.year+(b.month-1)/12);});
  var h=svgOpen(W,H,'tl');
  h+='<line x1="'+axisX+'" y1="'+top+'" x2="'+axisX+'" y2="'+(H-bottom)+'" class="axis"/>';
  for(var y=2017;y<=2027;y++){
    h+='<line x1="'+(axisX-5)+'" y1="'+Y(y,1)+'" x2="'+(axisX+5)+'" y2="'+Y(y,1)+'" class="tick"/>'+
       '<text x="'+(axisX-12)+'" y="'+(Y(y,1)+4)+'" class="axt" text-anchor="end">'+y+'</text>';
  }
  var now=Y(2026,9);
  h+='<line x1="'+(axisX-40)+'" y1="'+now+'" x2="'+(W-20)+'" y2="'+now+'" class="now"/>'+
     '<text x="'+(W-20)+'" y="'+(now-6)+'" class="axl" text-anchor="end">today</text>';
  var lastLabel=-999, body='';
  ev.forEach(function(e){
    var y=Y(e.year,e.month), ly=Math.max(y,lastLabel+minGap); lastLabel=ly;
    var tip=e.label+' ('+e.year+').';
    h+='<line x1="'+axisX+'" y1="'+y+'" x2="'+(dotX-6)+'" y2="'+y+'" class="stem"/>';
    h+='<line x1="'+(dotX+7)+'" y1="'+y+'" x2="'+(dotX+26)+'" y2="'+ly+'" class="stem"/>';
    if(e.kind==='out') h+='<circle cx="'+dotX+'" cy="'+y+'" r="5" class="dot out"'+tipAttr(tip)+'/>';
    else if(e.kind==='icon') h+='<rect x="'+(dotX-5)+'" y="'+(y-5)+'" width="10" height="10" class="dot icon"'+tipAttr(tip)+'/>';
    else h+='<circle cx="'+dotX+'" cy="'+y+'" r="5" class="dot in"'+tipAttr(tip)+'/>';
    h+='<text x="'+(dotX+32)+'" y="'+(ly+4)+'" class="evl">'+esc(e.label)+
       ' <tspan class="cnt">'+MONTHS[e.month-1]+' '+e.year+'</tspan></text>';
  });
  H=Math.max(H,lastLabel+bottom);
  h=h.replace(/viewBox="0 0 \d+ \d+"/,'viewBox="0 0 '+W+' '+Math.ceil(H)+'"');
  h+='</svg>';
  var leg='<div class="flegend"><i><span class="dk in"></span>Entry or launch</i><i><span class="dk out"></span>Closure, sale or filing</i><i><span class="dk icon"></span>ICON</i></div>';
  var tbl='<table class="ftab"><thead><tr><th>When</th><th>Event</th></tr></thead><tbody>'+
    ev.map(function(e){return '<tr><td>'+MONTHS[e.month-1]+' '+e.year+'</td><td>'+esc(e.label)+'</td></tr>';}).join('')+'</tbody></table>';
  return figure('The field, 2017 to 2027', 'Entries, closures and ICON’s own dates, from company releases, filings and trade press.', leg+h, tbl);
}
var MONTHS=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

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

function figure(title,caption,body,table){
  return '<section class="figs"><h3>'+esc(title)+'</h3><p class="fcap">'+esc(caption)+'</p>'+
    '<div class="fwrap">'+body+'</div>'+
    '<details class="ftable"><summary>As a table</summary>'+table+'</details></section>';
}

var W_=W;
function drawMarket(){
  var n=T.length, yes=T.filter(function(t){return t.marks.innovation==='clear';}).length;
  var fit=T.filter(function(t){return t.marks.machine_fit==='clear';}).length;
  var both=T.filter(function(t){return t.marks.machine_fit==='clear'&&t.marks.innovation!=='fail';}).length;
  var dec=T.filter(function(t){return t.decider_confirmed;}).length;
  document.getElementById('mkStats').innerHTML=[
    [n,'firms screened'],[fit,'a Yes on Printer fit'],[both,'a Yes on Printer fit with a track record'],
    [yes,'have paid for a new method before'],[dec,'with a confirmed decision-maker']
  ].map(function(s){return '<div class="stat"><b>'+s[0]+'</b><span>'+esc(s[1])+'</span></div>';}).join('');
  var M=D.method||[],BM=D.bands_method||{};
  var method='<section class="figs method"><h3>How each number is produced</h3><dl>'+
    M.map(function(m){return '<dt>'+esc(m.title)+'</dt><dd>'+esc(m.text)+
      (m.title==='Machine-fit bands'?' '+(BM.sources||[]).map(function(s){
        return '<a class="src" href="'+esc(s.url)+'" target="_blank" rel="noopener">'+esc(s.label)+'</a>';}).join(' '):'')+
      '</dd>';}).join('')+'</dl></section>';
  document.getElementById('mkBody').innerHTML=figClosings()+figSections()+figOwners()+figPrinted()+figTimeline()+method;
  if(SEG_OPEN) showSegment(SEG_OPEN);
}

/* one tooltip for every mark */
(function(){
  var tip=document.createElement('div');tip.id='tip';tip.setAttribute('role','tooltip');tip.hidden=true;
  document.body.appendChild(tip);
  function show(e){var el=e.target.closest&&e.target.closest('[data-tip]'); if(!el){tip.hidden=true;return;}
    tip.textContent=el.getAttribute('data-tip');tip.hidden=false;move(e);}
  function move(e){var x=e.clientX+14,y=e.clientY+14;
    var r=tip.getBoundingClientRect();
    if(x+r.width>window.innerWidth-12) x=e.clientX-r.width-14;
    if(y+r.height>window.innerHeight-12) y=e.clientY-r.height-14;
    tip.style.left=x+'px';tip.style.top=y+'px';}
  document.addEventListener('mouseover',show);
  document.addEventListener('mousemove',function(e){if(!tip.hidden)move(e);});
  document.addEventListener('mouseout',function(e){if(e.target.closest&&e.target.closest('[data-tip]'))tip.hidden=true;});
})();
