// FeaturedCollection.jsx
const OBJECTS = [
  { id: 1, title: 'Meridian 01', kind: 'Chronometer', price: '€ 4,200', tag: 'Atelier', note: 'Brushed sterling · 38mm' },
  { id: 2, title: 'Tide Compass', kind: 'Instrument', price: '€ 1,680', tag: 'Limited', note: 'Cast bronze · azimuth' },
  { id: 3, title: 'Abyss Journal', kind: 'Paper goods', price: '€ 220', tag: 'In stock', note: 'Deckle-edge · N4 plate' },
];

const ObjectCard = ({ o, onOpen }) => (
  <article onClick={onOpen} style={{
    background: 'var(--ink-current)',
    border: '1px solid var(--border-2)',
    borderRadius: 6, overflow: 'hidden',
    cursor: 'pointer',
    transition: 'all 320ms cubic-bezier(.22,.61,.36,1)',
  }}
  onMouseEnter={e => {
    e.currentTarget.style.transform = 'translateY(-4px)';
    e.currentTarget.style.borderColor = 'rgba(63,212,224,.4)';
    e.currentTarget.style.boxShadow = '0 16px 48px rgba(0,0,0,.5), 0 0 24px rgba(63,212,224,.1)';
  }}
  onMouseLeave={e => {
    e.currentTarget.style.transform = '';
    e.currentTarget.style.borderColor = 'var(--border-2)';
    e.currentTarget.style.boxShadow = '';
  }}>
    {/* image placeholder — evokes a studio object photo */}
    <div style={{
      aspectRatio: '4/5', position: 'relative',
      background: 'linear-gradient(160deg, #1A4E5E 0%, #0E2B36 60%, #061419 100%)',
      borderBottom: '1px solid var(--border-1)',
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      overflow: 'hidden',
    }}>
      <div style={{position:'absolute',inset:0,backgroundImage:'url(../../assets/bg-neural-network.png)',backgroundSize:'cover',opacity:.15}}/>
      <div style={{position:'absolute',inset:0,background:'radial-gradient(ellipse at 50% 40%, rgba(205,206,210,.08), transparent 60%)'}}/>
      <img src="../../assets/logo-star.png" alt="" style={{width:96,height:96,objectFit:'contain',opacity:.9,filter:'drop-shadow(0 6px 22px rgba(0,0,0,.6)) drop-shadow(0 0 30px rgba(63,212,224,.15))',position:'relative'}}/>
      <div style={{position:'absolute',top:14,left:14}}><Tag tone={o.tag==='Limited'?'accent':'neutral'}>{o.tag}</Tag></div>
    </div>
    <div style={{padding:'20px 22px'}}>
      <div style={{fontFamily:'Inter',fontSize:10,fontWeight:500,textTransform:'uppercase',letterSpacing:'.22em',color:'var(--fg-3)'}}>{o.kind}</div>
      <h3 style={{fontFamily:'Cormorant Garamond',fontStyle:'italic',fontWeight:400,fontSize:26,color:'var(--fg-1)',margin:'6px 0 4px'}}>{o.title}</h3>
      <p style={{fontFamily:'Inter',fontSize:12,color:'var(--fg-3)',margin:'0 0 14px'}}>{o.note}</p>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',paddingTop:14,borderTop:'1px solid var(--border-1)'}}>
        <span style={{fontFamily:'JetBrains Mono',fontSize:12,color:'var(--fg-2)'}}>{o.price}</span>
        <span style={{fontFamily:'Inter',fontSize:10,fontWeight:500,letterSpacing:'.18em',textTransform:'uppercase',color:'var(--glow-cyan)'}}>View →</span>
      </div>
    </div>
  </article>
);

const FeaturedCollection = ({ onOpen }) => (
  <section style={{padding: '120px 48px', maxWidth: 1240, margin: '0 auto'}}>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-end',marginBottom:56}}>
      <div>
        <Eyebrow>✦  Collection · MMXXVI</Eyebrow>
        <h2 style={{
          fontFamily:'Cormorant Garamond',fontStyle:'italic',fontWeight:400,
          fontSize:56,lineHeight:1.05,letterSpacing:'-0.015em',
          color:'var(--fg-1)',margin:'20px 0 0',maxWidth:'16ch',
        }}>Struck by hand, calibrated under tide.</h2>
      </div>
      <a href="#" onClick={(e)=>{e.preventDefault();onOpen && onOpen();}} style={{fontFamily:'Inter',fontSize:11,fontWeight:500,letterSpacing:'.22em',textTransform:'uppercase',color:'var(--glow-cyan)',textDecoration:'none'}}>The full atlas →</a>
    </div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:24}}>
      {OBJECTS.map(o => <ObjectCard key={o.id} o={o} onOpen={() => onOpen && onOpen(o)} />)}
    </div>
  </section>
);

Object.assign(window, { FeaturedCollection, ObjectCard, OBJECTS });
