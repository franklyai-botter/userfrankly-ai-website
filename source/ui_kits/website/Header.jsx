// Header.jsx
const Header = ({ current, onNav }) => {
  const [scrolled, setScrolled] = React.useState(false);
  React.useEffect(() => {
    const el = document.querySelector('.site-scroll') || window;
    const onScroll = () => {
      const y = el.scrollTop || window.scrollY || 0;
      setScrolled(y > 40);
    };
    el.addEventListener('scroll', onScroll);
    return () => el.removeEventListener('scroll', onScroll);
  }, []);

  const link = (id, label) => (
    <a href="#" onClick={(e) => { e.preventDefault(); onNav(id); }}
       style={{
         fontFamily: 'Inter', fontSize: 11, fontWeight: 500,
         textTransform: 'uppercase', letterSpacing: '0.22em',
         color: current === id ? 'var(--glow-cyan)' : 'var(--fg-2)',
         textDecoration: 'none', padding: '8px 0',
         borderBottom: current === id ? '1px solid var(--glow-cyan)' : '1px solid transparent',
         transition: 'all 180ms',
       }}>{label}</a>
  );

  return (
    <header style={{
      position: 'sticky', top: 0, zIndex: 20,
      background: scrolled ? 'rgba(10,32,40,0.78)' : 'transparent',
      backdropFilter: scrolled ? 'blur(24px)' : 'none',
      WebkitBackdropFilter: scrolled ? 'blur(24px)' : 'none',
      borderBottom: scrolled ? '1px solid rgba(205,206,210,.1)' : '1px solid transparent',
      transition: 'all 320ms cubic-bezier(.22,.61,.36,1)',
    }}>
      <div style={{
        maxWidth: 1240, margin: '0 auto',
        padding: '20px 48px',
        display: 'flex', alignItems: 'center', gap: 32,
      }}>
        <a href="#" onClick={(e)=>{e.preventDefault();onNav('home')}} style={{display:'flex',alignItems:'center',gap:12,textDecoration:'none',border:0}}>
          <img src="../../assets/logo-star.png" alt="" style={{width:32,height:32,objectFit:'contain'}}/>
          <div style={{display:'flex',flexDirection:'column',lineHeight:1}}>
            <span style={{fontFamily:'Italiana',fontSize:18,color:'var(--fg-1)',letterSpacing:'.04em'}}>Neural Nautic</span>
            <span style={{fontFamily:'Inter',fontSize:9,color:'var(--fg-3)',letterSpacing:'.28em',textTransform:'uppercase',marginTop:2}}>Atelier · est. MMXXV</span>
          </div>
        </a>
        <nav style={{display:'flex',gap:28,marginLeft:'auto'}}>
          {link('home', 'Atelier')}
          {link('collection', 'Collection')}
          {link('journal', 'Log')}
          {link('detail', 'Charts')}
        </nav>
        <Button variant="secondary">Sign in</Button>
      </div>
    </header>
  );
};

window.Header = Header;
