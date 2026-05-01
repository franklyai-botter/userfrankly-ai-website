// atoms.jsx — small reusable pieces
const Eyebrow = ({ children, accent = true }) => (
  <span style={{
    fontFamily: 'Inter, sans-serif',
    fontSize: 11, fontWeight: 500,
    textTransform: 'uppercase',
    letterSpacing: '0.24em',
    color: accent ? 'var(--glow-cyan)' : 'var(--fg-3)',
  }}>{children}</span>
);

const Button = ({ children, variant = 'primary', onClick, icon }) => {
  const base = {
    fontFamily: 'Inter, sans-serif', fontSize: 13, fontWeight: 500,
    letterSpacing: '0.06em', padding: '13px 24px', borderRadius: 4,
    cursor: 'pointer', transition: 'all 180ms cubic-bezier(.22,.61,.36,1)',
    display: 'inline-flex', alignItems: 'center', gap: 10,
    border: '1px solid transparent',
  };
  const styles = {
    primary: { ...base, background: 'var(--glow-cyan)', color: 'var(--ink-abyss)', boxShadow: 'inset 0 1px 0 rgba(255,255,255,.3), 0 0 24px rgba(63,212,224,.25)' },
    secondary: { ...base, background: 'transparent', color: 'var(--fg-1)', borderColor: 'rgba(205,206,210,.4)' },
    ghost: { ...base, background: 'transparent', color: 'var(--glow-cyan)', padding: '13px 14px' },
    brushed: { ...base, background: 'linear-gradient(180deg,#1A4E5E,#0E2B36)', color: 'var(--fg-1)', borderColor: 'rgba(205,206,210,.2)', borderRadius: 999, boxShadow: 'inset 0 1px 0 rgba(255,255,255,.08), inset 0 -1px 0 rgba(0,0,0,.3)' },
  };
  return <button style={styles[variant]} onClick={onClick}>{children}{icon && <span style={{fontFamily:'serif'}}>{icon}</span>}</button>;
};

const Tag = ({ children, tone = 'neutral' }) => {
  const tones = {
    neutral: { bg: 'rgba(205,206,210,.08)', fg: '#CDCED2', border: 'rgba(205,206,210,.18)' },
    accent: { bg: 'rgba(63,212,224,.12)', fg: '#6FEFF5', border: 'rgba(63,212,224,.3)' },
    ok: { bg: 'rgba(111,239,199,.1)', fg: '#6FEFC7', border: 'rgba(111,239,199,.3)' },
  };
  const t = tones[tone];
  return <span style={{
    fontFamily:'Inter',fontSize:11,fontWeight:500,letterSpacing:'.08em',
    padding:'4px 12px',borderRadius:999,
    background:t.bg,color:t.fg,border:`1px solid ${t.border}`,
    display:'inline-flex',alignItems:'center',gap:6,
  }}>{children}</span>;
};

const Rule = ({ width = 40, color = 'var(--glow-cyan)' }) => (
  <div style={{ width, height: 1, background: color }} />
);

const Icon = ({ path, size = 18, color = 'currentColor', sw = 1.5 }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round">
    <path d={path} />
  </svg>
);

Object.assign(window, { Eyebrow, Button, Tag, Rule, Icon });
