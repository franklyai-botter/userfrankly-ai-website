// ObjectDetail.jsx — a single object's chart
const ObjectDetail = ({ o, onBack }) => {
  const obj = o || { title: 'Meridian 01', kind: 'Chronometer', price: '€ 4,200', note: 'Brushed sterling · 38mm', tag: 'Atelier' };
  return (
    <section style={{padding:'80px 48px 120px',maxWidth:1240,margin:'0 auto'}}>
      <button onClick={onBack} style={{background:'none',border:0,color:'var(--fg-3)',fontFamily:'Inter',fontSize:11,letterSpacing:'.22em',textTransform:'uppercase',cursor:'pointer',marginBottom:40,padding:0}}>← Return to shore</button>
      <div style={{display:'grid',gridTemplateColumns:'1.1fr 1fr',gap:72,alignItems:'start'}}>
        {/* image */}
        <div style={{
          aspectRatio:'4/5',position:'relative',
          background:'linear-gradient(160deg, #1A4E5E 0%, #0E2B36 60%, #061419 100%)',
          border:'1px solid var(--border-2)',borderRadius:6,overflow:'hidden',
          boxShadow:'0 32px 80px rgba(0,0,0,.55)',
        }}>
          <div style={{position:'absolute',inset:0,backgroundImage:'url(../../assets/bg-neural-network.png)',backgroundSize:'cover',opacity:.25}}/>
          <div style={{position:'absolute',inset:0,background:'radial-gradient(ellipse at 50% 45%, rgba(205,206,210,.1), transparent 60%)'}}/>
          <img src="../../assets/logo-star.png" alt="" style={{position:'absolute',inset:0,margin:'auto',width:240,height:240,objectFit:'contain',filter:'drop-shadow(0 10px 40px rgba(0,0,0,.7)) drop-shadow(0 0 48px rgba(63,212,224,.18))'}}/>
          <div style={{position:'absolute',bottom:20,left:20,fontFamily:'JetBrains Mono',fontSize:10,color:'var(--fg-3)',letterSpacing:'.12em'}}>PLATE · 001 / 012</div>
        </div>
        {/* spec */}
        <div>
          <Tag tone={obj.tag==='Limited'?'accent':'neutral'}>{obj.tag}</Tag>
          <div style={{fontFamily:'Inter',fontSize:11,fontWeight:500,textTransform:'uppercase',letterSpacing:'.24em',color:'var(--fg-3)',marginTop:24}}>{obj.kind}</div>
          <h1 style={{fontFamily:'Italiana',fontSize:72,lineHeight:1.02,letterSpacing:'-0.015em',color:'var(--fg-1)',margin:'8px 0 20px'}}>{obj.title}</h1>
          <p style={{fontFamily:'Cormorant Garamond',fontStyle:'italic',fontSize:22,lineHeight:1.55,color:'var(--fg-2)',maxWidth:'52ch',margin:'0 0 32px'}}>
            A quiet instrument — struck in brushed sterling, calibrated by hand under tide. One of twelve in the current run.
          </p>
          <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:0,margin:'32px 0',borderTop:'1px solid var(--border-1)'}}>
            {[
              ['Material','Sterling · 925'],
              ['Diameter','38 mm'],
              ['Bearing','N 52° 22′'],
              ['Edition','1 of 12'],
              ['Struck','Atelier, Amsterdam'],
              ['Delivery','By hand'],
            ].map(([k,v],i)=>(
              <div key={i} style={{padding:'16px 0',borderBottom:'1px solid var(--border-1)',display:'flex',justifyContent:'space-between',paddingRight:i%2===0?24:0,paddingLeft:i%2===1?24:0,borderLeft:i%2===1?'1px solid var(--border-1)':0}}>
                <span style={{fontFamily:'Inter',fontSize:10,fontWeight:500,textTransform:'uppercase',letterSpacing:'.2em',color:'var(--fg-3)'}}>{k}</span>
                <span style={{fontFamily:'JetBrains Mono',fontSize:12,color:'var(--fg-1)'}}>{v}</span>
              </div>
            ))}
          </div>
          <div style={{display:'flex',alignItems:'center',gap:18,marginTop:24}}>
            <span style={{fontFamily:'Italiana',fontSize:32,color:'var(--fg-1)'}}>{obj.price}</span>
            <Button variant="primary" icon="→">Cast off</Button>
            <Button variant="ghost">Save to log</Button>
          </div>
        </div>
      </div>
    </section>
  );
};

window.ObjectDetail = ObjectDetail;
