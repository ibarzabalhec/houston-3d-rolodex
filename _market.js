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
var NB=(D.market&&D.market.closings_base)||0;
function figClosings(){
  var rows=MK.closings||[]; if(!rows.length) return '';
  var W=900,L=190,R=110,rowH=30,top=26,H=top+rows.length*rowH+30;
  var max=1200, X=function(v){return L+(W-L-R)*Math.min(v,max)/max;};
  var h=svgOpen(W,H);
  // gridlines
  [0,200,400,600,800,1000,1200].forEach(function(v){
    h+='<line x1="'+X(v)+'" y1="'+(top-8)+'" x2="'+X(v)+'" y2="'+(top+rows.length*rowH)+'" class="grid"/>'+
       '<text x="'+X(v)+'" y="'+(top+rows.length*rowH+18)+'" class="axt">'+fmt(v)+'</text>';
  });
  rows.forEach(function(r,i){
    var y=top+i*rowH, bh=18, cy=y+bh/2;
    var tip=r.name+': '+(r.low===r.high?fmt(r.high):fmt(r.low)+' to '+fmt(r.high))+
            ' homes a year, '+r.year+'. '+r.source+'.';
    h+='<text x="'+(L-10)+'" y="'+(cy+4)+'" class="rowl" text-anchor="end" data-id="'+r.id+'">'+esc(r.short)+'</text>';
    h+='<rect x="'+X(0)+'" y="'+y+'" width="'+(X(r.low)-X(0))+'" height="'+bh+'" rx="0" class="bar"'+tipAttr(tip)+'/>';
    if(r.high>r.low){
      h+='<line x1="'+X(r.low)+'" y1="'+cy+'" x2="'+X(r.high)+'" y2="'+cy+'" class="range"'+tipAttr(tip)+'/>'+
         '<line x1="'+X(r.high)+'" y1="'+(cy-5)+'" x2="'+X(r.high)+'" y2="'+(cy+5)+'" class="range"/>';
    }
    h+='<text x="'+(X(r.high)+8)+'" y="'+(cy+4)+'" class="val">'+
       (r.low===r.high?fmt(r.high):fmt(r.low)+'–'+fmt(r.high))+' <tspan class="yr">'+r.year+'</tspan></text>';
  });
  h+='</svg>';
  var tbl='<table class="ftab"><thead><tr><th>Firm</th><th class="num">Homes a year</th><th>Year</th><th>Source</th></tr></thead><tbody>'+
    rows.map(function(r){return '<tr><td>'+esc(r.name)+'</td><td class="num">'+(r.low===r.high?fmt(r.high):fmt(r.low)+' to '+fmt(r.high))+
      '</td><td>'+r.year+'</td><td>'+esc(r.source)+'</td></tr>';}).join('')+'</tbody></table>';
  return figure('Published annual closings',
    'How big each builder actually is, in houses closed a year. '+rows.length+' of the '+NB+
    ' builders on the deck publish a figure; the rest do not and are not drawn. Contractors close no houses and are not counted. A range is drawn to its low end with a line to its high end.',
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


/* ------------------------------------------------------------- permits
   A different quantity from everything above. Census counts units AUTHORISED
   BY PERMIT; the closings chart counts houses handed over by a builder. They
   are never added, divided or drawn on one axis. Magnitude here is grey to
   ink: the accent stays reserved for the third count. */
var PM=D.permits||{};
var PSRC=PM.sources||[];
function psrc(){var a=[].slice.call(arguments);
  return PSRC.filter(function(s){return a.some(function(k){return s.url.indexOf(k)>-1;});});}
var RAMP=['#EDEDED','#D6D6D6','#B6B6B6','#8A8A8A','#4F4F4F','#111111'];
function shade(v,max){ /* 0..1 -> paper to ink, five steps, printable */
  if(!max) return RAMP[0];
  var t=Math.sqrt(v/max), i=Math.min(5,Math.floor(t*5.999));
  return RAMP[i];
}
function inkOn(hex){return (hex==='#4F4F4F'||hex==='#111111')?'#FFFFFF':'#111111';}

/* 7. The metro series. One column a year, single family only. */
function figPermits(){
  var rows=PM.msa||[]; if(!rows.length) return '';
  var W=940,L=58,R=16,T=30,B=46,H=T+250+B;
  var max=Math.max.apply(null,rows.map(function(r){return r.sf;}));
  var bw=(W-L-R)/rows.length;
  var X=function(i){return L+i*bw;}, Y=function(v){return T+250-250*v/max;};
  var h=svgOpen(W,H);
  [0,10000,20000,30000,40000,50000].forEach(function(v){
    h+='<line x1="'+L+'" y1="'+Y(v)+'" x2="'+(W-R)+'" y2="'+Y(v)+'" class="grid"/>'+
       '<text x="'+(L-8)+'" y="'+(Y(v)+4)+'" class="axt" text-anchor="end">'+fmt(v)+'</text>';
  });
  rows.forEach(function(r,i){
    var tip=r.year+': '+fmt(r.sf)+' single-family units authorised, '+fmt(r.all)+' units of all types.';
    h+='<rect x="'+(X(i)+1)+'" y="'+Y(r.sf)+'" width="'+(bw-2)+'" height="'+(T+250-Y(r.sf))+
       '" class="bar"'+tipAttr(tip)+'/>';
    if(r.year%5===0)
      h+='<text x="'+(X(i)+bw/2)+'" y="'+(T+250+16)+'" class="axt">'+r.year+'</text>';
  });
  h+='<line x1="'+L+'" y1="'+(T+250)+'" x2="'+(W-R)+'" y2="'+(T+250)+'" class="axis"/></svg>';
  var tbl='<table class="ftab"><thead><tr><th>Year</th><th>Single family</th><th>All units</th></tr></thead><tbody>'+
    rows.slice().reverse().map(function(r){return '<tr><td>'+r.year+'</td><td>'+fmt(r.sf)+'</td><td>'+fmt(r.all)+'</td></tr>';}).join('')+
    '</tbody></table>';
  var g=PM.geo||{};
  return figure('Single-family units authorised, '+(g.name||''),
    'Building permits issued across the ten counties, 1980 to '+rows[rows.length-1].year+
    '. A permit is an authorisation, not a completed house and not a closing: the builder figures below count houses handed over. Census counts townhouses and row houses as single family.',
    h, tbl, psrc('huduser','definitions'));
}

/* 8. The ten counties, drawn. Outlines are TxDOT's, at a fidelity where a shared
   border between two counties lands on the same pixel, so the seam reads as one
   line. Fill is the sequential ramp; labels sit at each county's pole of
   inaccessibility rather than its centroid, so they stay inside the shape. */
var PYEAR=2025;
function figCountyMap(){
  var G=PM.geom||[], C=PM.counties||[]; if(!G.length||!C.length) return '';
  var yrs=C[0].years, W=680,H=470, PAD=26;
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
  function labelPoint(r){
    var x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;
    r.forEach(function(p){x0=Math.min(x0,p[0]);y0=Math.min(y0,p[1]);x1=Math.max(x1,p[0]);y1=Math.max(y1,p[1]);});
    var best=null, bd=-1, step=Math.max((x1-x0),(y1-y0))/22;
    function scan(cx0,cy0,cx1,cy1,st){
      for(var x=cx0;x<=cx1;x+=st) for(var y=cy0;y<=cy1;y+=st){
        if(!inside(x,y,r)) continue;
        var d=1e9;
        for(var i=0,j=r.length-1;i<r.length;j=i++){
          d=Math.min(d,ptSeg(x,y,r[i][0],r[i][1],r[j][0],r[j][1]));
          if(d<bd) break;
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
  var ANCHOR={};
  G.forEach(function(f){
    var big=null, ba=-1;
    f.rings.forEach(function(poly){
      var r=poly[0], a=0;
      for(var j=0;j<r.length;j++){var q=r[j],w=r[(j+1)%r.length];a+=q[0]*w[1]-w[0]*q[1];}
      a=Math.abs(a/2); if(a>ba){ba=a;big=r;}
    });
    ANCHOR[f.fips]=labelPoint(big.map(PX));
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
         tipAttr(c.name+' County, '+PYEAR+': '+fmt(v)+' single-family units authorised')+'/>';
    });
    h+='</g><g class="ctyedge">'+G.map(function(f){return '<path d="'+D_[f.fips]+'"/>';}).join('')+
       '</g><g class="ctyls">';
    G.forEach(function(f){
      var c=C.filter(function(x){return x.fips===f.fips;})[0]; if(!c) return;
      var v=c.sf[i], fill=shade(v,max), A=ANCHOR[f.fips], x=A.p[0], y=A.p[1];
      var tight=A.r<30, fs=tight?10:12, vs=tight?9:10.5;
      var pen=' fill="'+inkOn(fill)+'" stroke="'+fill+'" stroke-width="'+(tight?2.4:3)+'"';
      h+='<text x="'+x.toFixed(0)+'" y="'+(y-2).toFixed(0)+'" class="ctyl" style="font-size:'+fs+'px"'+pen+'>'+esc(c.name)+'</text>'+
         '<text x="'+x.toFixed(0)+'" y="'+(y+(tight?9:12)).toFixed(0)+'" class="ctyv" style="font-size:'+vs+'px"'+pen+'>'+fmt(v)+'</text>';
    });
    h+='</g>';
    /* key: a continuous strip, two labels, no ladder of numbers */
    var KW=170, kx=14, ky=H-34;
    h+='<text x="'+kx+'" y="'+(ky-9)+'" class="axl">Units authorised, '+PYEAR+'</text>';
    RAMP.forEach(function(fill,b){
      h+='<rect x="'+(kx+b*(KW/6)).toFixed(1)+'" y="'+ky+'" width="'+(KW/6).toFixed(1)+'" height="9" fill="'+fill+'" '+
         'stroke="#CFCFCF" stroke-width=".5"/>';
    });
    h+='<text x="'+kx+'" y="'+(ky+20)+'" class="axs">0</text>'+
       '<text x="'+(kx+KW)+'" y="'+(ky+20)+'" class="axe">'+fmt(max)+'</text>';
    h+='</svg>';
    var host=document.getElementById('mapHost'); if(host) host.innerHTML=h;
  };
  return figure('Where the permits are',
    'Single-family units authorised by county, on a square-root scale so the middle of the range stays legible next to Harris. Outlines are TxDOT’s. Drag the year.',
    body, tbl, psrc('huduser','txdot'), 'figMap');
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
    var cw=Math.max(26,Math.min(34,(900-170)/yrs.length)), rh=30, L=170, T=26;
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
      h+='<text x="'+(L-10)+'" y="'+(T+r*rh+rh/2+4)+'" class="rowl" text-anchor="end">'+esc(c.name)+'</text>';
      c.sf.forEach(function(v,i){
        var m=mi[yrs[i]];
        var val=(PMODE==='shr')?(m?v/m:0):(peak[c.fips]?v/peak[c.fips]:0);
        var fill=shade(val,max);
        var tip=c.name+' County, '+yrs[i]+': '+fmt(v)+' single-family units authorised'+
          (m?', '+(100*v/m).toFixed(1)+' per cent of the metro':'')+'.';
        h+='<rect x="'+(L+i*cw)+'" y="'+(T+r*rh)+'" width="'+(cw-2)+'" height="'+(rh-2)+
           '" fill="'+fill+'" class="cell"'+tipAttr(tip)+'/>';
      });
    });
    h+='</svg>';
    var host=document.getElementById('mtxHost'); if(host) host.innerHTML=h;
  };
  return figure('The same counties, year by year',
    'Every county across '+yrs[0]+' to '+yrs[yrs.length-1]+'. Share of metro shades each county-year against the metro total for that year, so a county gaining ground darkens even while Harris stays the largest. Against its own peak shades each row against that county\u2019s own busiest year, which is the cycle rather than the rank. Units are in the tooltip and in the table.',
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
    var W=900,L=260,R=90,rowH=24,T=14,H=T+rows.length*rowH+18;
    var max=Math.max.apply(null,rows.map(function(r){return r.sf[i];}));
    var X=function(v){return L+(W-L-R)*v/max;};
    var h=svgOpen(W,H);
    rows.forEach(function(p,r){
      var y=T+r*rowH, tip=p.name+', '+p.county+' County, '+JYEAR+': '+fmt(p.sf[i])+' single-family units authorised.';
      h+='<text x="'+(L-10)+'" y="'+(y+14)+'" class="rowl sm" text-anchor="end">'+esc(p.name)+'</text>'+
         '<rect x="'+L+'" y="'+(y+3)+'" width="'+(X(p.sf[i])-L)+'" height="'+(rowH-9)+'" class="bar'+
         (/Unincorporated/i.test(p.name)?' uninc':'')+'"'+tipAttr(tip)+'/>'+
         '<text x="'+(X(p.sf[i])+8)+'" y="'+(y+14)+'" class="val">'+fmt(p.sf[i])+'</text>';
    });
    h+='</svg>';
    var host=document.getElementById('jurHost'); if(host) host.innerHTML=h;
  };
  return figure('Which jurisdiction issues the permit',
    P.length+' permit-issuing jurisdictions sit inside the metro and they sum to the ten counties exactly. The top 25 are drawn; all of them are in the table. Outlined bars are unincorporated county area, where the county issues the permit and no city does; solid bars are a city. On this evidence most single-family permitting in Greater Houston happens outside a city limit.',
    body, tbl, psrc('huduser'));
}

function figure(title,caption,body,table,sources,id){
  var src=(sources||[]).map(function(s){
    return '<a class="src" href="'+esc(s.url)+'" target="_blank" rel="noopener">'+esc(s.label)+'</a>';}).join('');
  return '<section class="figs"'+(id?' id="'+id+'"':'')+'><h3>'+esc(title)+'</h3>'+
    '<p class="fcap">'+esc(caption)+'</p>'+
    '<div class="fwrap">'+body+'</div>'+
    (src?'<p class="figsrc"><span class="lab">Source</span>'+src+'</p>':'')+
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
  document.getElementById('mkBody').innerHTML=
    figPermits()+figCountyMap()+figCountyMatrix()+figPlaces()+
    figClosings()+figSections()+figOwners()+figPrinted()+figTimeline();
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
