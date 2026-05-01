// Footer.jsx
const Footer = () => (
  <footer style={{
    position:'relative',overflow:'hidden',
    background:'var(--ink-abyss)',
    padding:'96px 48px 40px',
    marginTop:80,borderTop:'1px solid var(--border-1)',
  }}>
    <div style={{position:'absolute',inset:0,backgroundImage:'url(../../assets/bg-neural-network.png)',backgroundSize:'cover',opacity:.2}}/>
    <div style={{position:'absolute',inset:0,background:'linear-gradient(180deg, rgba(6,20,25,.3), rgba(6,20,25,.95) 80%)'}}/>

    <div style={{position:'relative',maxWidth:1240,margin:'0 auto'}}>
      <div style={{display:'grid',gridTemplateColumns:'2fr 1fr 1fr 1fr',gap:48,marginBottom:72}}>
        <div>
          <div style={{display:'flex',alignItems:'center',gap:12}}>
            <img src="../../assets/logo-star.png" alt="" style={{width:40,height:40,objectFit:'contain'}}/>
            <span style={{fontFamily:'Italiana',fontSize:22,color:'var(--fg-1)',letterSpacing:'.04em'}}>Neural Nautic</span>
          </div>
          <p style={{fontFamily:'Cormorant Garamond',fontStyle:'italic',fontSize:18,color:'var(--fg-2)',lineHeight:1.55,marginTop:20,maxWidth:'38ch'}}>
            A small atelier, keeping a slow log. Goods and software, forged in brushed platinum.
          </p>
        </div>
        {[
          ['Atelier',['The workshop','The log','Commissions','Press']],
          ['Collection',['Chronometers','Instruments','Paper goods','Archive']],
          ['Waypoints',['Contact','Mailing list','Charts','Copyright']],
        ].map(([h,items])=>(
          <div key={h}>
            <div style={{fontFamily:'Inter',fontSize:10,fontWeight:500,textTransform:'uppercase',letterSpacing:'.24em',color:'var(--glow-cyan)',marginBottom:18}}>{h}</div>
            {items.map(it=><a key={it} href="#" style={{display:'block',fontFamily:'Inter',fontSize:13,color:'var(--fg-2)',textDecoration:'none',padding:'6px 0',border:0}}>{it}</a>)}
          </div>
        ))}
      </div>

      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',paddingTop:32,borderTop:'1px solid var(--border-1)'}}>
        <div style={{fontFamily:'JetBrains Mono',fontSize:10,color:'var(--fg-3)',letterSpacing:'.12em'}}>© MMXXVI · Neural Nautic Atelier · Amsterdam · N 52°22′</div>
        <div style={{fontFamily:'Inter',fontSize:10,fontWeight:500,textTransform:'uppercase',letterSpacing:'.24em',color:'var(--fg-3)'}}>✦  A quiet gleam</div>
      </div>
    </div>
  </footer>
);

window.Footer = Footer;
