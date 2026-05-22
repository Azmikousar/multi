import { useState } from "react";

const themes = {
  dark: {
    bgPrimary: "#07090F",
    bgSecondary: "#0D1017",
    bgCard: "#10131D",
    bgCardHover: "#151a28",
    border: "#1C2236",
    accent: "#5B8DEF",
    accent2: "#A259FF",
    accentGlow: "rgba(91,141,239,0.15)",
    textPrimary: "#EDF0F7",
    textSecondary: "#7A85A3",
    textMuted: "#3E4860",
    sidebar: "#090B13",
    tagBg: "rgba(91,141,239,0.11)",
    badgeBg: "rgba(162,89,255,0.13)",
    shine: "rgba(255,255,255,0.025)",
  },
  light: {
    bgPrimary: "#F4F6FC",
    bgSecondary: "#ECEEF7",
    bgCard: "#FFFFFF",
    bgCardHover: "#EEF1FB",
    border: "#D4D9EF",
    accent: "#3B6FD4",
    accent2: "#7C3AED",
    accentGlow: "rgba(59,111,212,0.12)",
    textPrimary: "#0F1624",
    textSecondary: "#4A5370",
    textMuted: "#9AA3BF",
    sidebar: "#ECEEF7",
    tagBg: "rgba(59,111,212,0.08)",
    badgeBg: "rgba(124,58,237,0.09)",
    shine: "rgba(255,255,255,0.6)",
  },
};

const pages = ["Home", "Chatbot", "Image Generator", "Document QA", "Content Generator"];

const tools = [
  { icon: "💬", title: "AI Chatbot", desc: "Ask questions, brainstorm ideas, get explanations in a seamless chat interface.", tag: "Gemini 2.0 Flash Lite" },
  { icon: "🎨", title: "Image Generator", desc: "Turn text prompts into stunning AI-generated visuals instantly.", tag: "Text → Image" },
  { icon: "📄", title: "Document QA", desc: "Upload any PDF and extract answers with AI-powered comprehension.", tag: "PDF · Instant" },
  { icon: "✍️", title: "Content Generator", desc: "Generate blogs, captions, emails, scripts and more in seconds.", tag: "6 Content Types" },
];

const features = ["Lightning-fast AI", "4 tools in one place", "Beginner friendly", "Modern workspace", "No account needed"];

const pageContent = {
  Chatbot: { badge: "Gemini 2.0 Flash Lite", title: "AI Chatbot", sub: "Ask anything — from quick facts to deep explanations, creative writing or code.", chips: ["⚡ Instant responses", "🧠 Contextual memory", "🚀 Smart conversations"] },
  "Image Generator": { badge: "Text to Image", title: "Image Generator", sub: "Describe anything and watch it materialise as an AI-generated visual.", chips: ["🎨 High quality", "⚡ Fast generation", "💾 Downloadable"] },
  "Document QA": { badge: "PDF Intelligence", title: "Document QA", sub: "Upload a PDF and ask questions — AI reads it so you don't have to.", chips: ["📄 PDF support", "🧠 AI comprehension", "📚 Smart Q&A"] },
  "Content Generator": { badge: "AI Writing", title: "Content Generator", sub: "Generate polished blogs, captions, emails, scripts, and more in seconds.", chips: ["⚡ Instant content", "🧠 Creative AI", "🚀 6 content types"] },
};

export default function App() {
  const [mode, setMode] = useState("dark");
  const [page, setPage] = useState("Home");
  const t = themes[mode];

  const css = {
    app: {
      display: "flex", minHeight: "100vh", fontFamily: "'DM Sans', sans-serif",
      background: t.bgPrimary, color: t.textPrimary,
      backgroundImage: `radial-gradient(ellipse 80% 50% at 15% 0%, ${t.accentGlow}, transparent), radial-gradient(ellipse 60% 40% at 85% 100%, rgba(162,89,255,0.06), transparent)`,
    },
    sidebar: {
      width: 220, flexShrink: 0, background: t.sidebar,
      borderRight: `1px solid ${t.border}`, padding: "28px 16px",
      display: "flex", flexDirection: "column", gap: 4,
    },
    logo: {
      fontFamily: "'Syne', sans-serif", fontWeight: 800, fontSize: 18,
      color: t.textPrimary, letterSpacing: "-0.02em",
      padding: "0 8px 20px", borderBottom: `1px solid ${t.border}`,
      marginBottom: 16,
    },
    logoAccent: {
      background: `linear-gradient(135deg, ${t.accent}, ${t.accent2})`,
      WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent",
    },
    navItem: (active) => ({
      padding: "9px 12px", borderRadius: 9, cursor: "pointer", fontSize: 14,
      fontWeight: active ? 600 : 400, color: active ? t.accent : t.textSecondary,
      background: active ? t.tagBg : "transparent",
      border: `1px solid ${active ? t.border : "transparent"}`,
      transition: "all 0.18s", letterSpacing: "0.01em",
      display: "flex", alignItems: "center", gap: 8,
    }),
    themeToggle: {
      marginTop: "auto", display: "flex", gap: 6,
      padding: "14px 0 0", borderTop: `1px solid ${t.border}`,
    },
    toggleBtn: (active) => ({
      flex: 1, padding: "7px 0", borderRadius: 8, border: `1px solid ${t.border}`,
      background: active ? t.tagBg : "transparent",
      color: active ? t.accent : t.textMuted,
      cursor: "pointer", fontSize: 12,
      fontFamily: "'Syne', sans-serif", fontWeight: 600,
      letterSpacing: "0.06em", transition: "all 0.18s",
    }),
    main: { flex: 1, padding: "40px 48px", overflowY: "auto", maxWidth: 900 },
  };

  const navIcons = { Home: "⌂", Chatbot: "💬", "Image Generator": "🎨", "Document QA": "📄", "Content Generator": "✍️" };

  return (
    <>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
        * { box-sizing: border-box; margin: 0; padding: 0; }
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: ${t.border}; border-radius: 4px; }
      `}</style>

      <div style={css.app}>
        {/* SIDEBAR */}
        <div style={css.sidebar}>
          <div style={css.logo}>
            Multi<span style={css.logoAccent}>GPT</span> <span style={{ fontSize: 13, color: t.textMuted, fontWeight: 400 }}>Studio</span>
          </div>

          {pages.map(p => (
            <div key={p} style={css.navItem(page === p)} onClick={() => setPage(p)}>
              <span>{navIcons[p]}</span> {p}
            </div>
          ))}

          <div style={css.themeToggle}>
            <button style={css.toggleBtn(mode === "light")} onClick={() => setMode("light")}>☀ Light</button>
            <button style={css.toggleBtn(mode === "dark")} onClick={() => setMode("dark")}>◑ Dark</button>
          </div>
        </div>

        {/* MAIN */}
        <div style={css.main}>
          {page === "Home" ? (
            <HomePage t={t} setPage={setPage} />
          ) : (
            <InnerPage t={t} page={page} data={pageContent[page]} />
          )}
        </div>
      </div>
    </>
  );
}

function HomePage({ t, setPage }) {
  return (
    <div>
      {/* Hero */}
      <div style={{ textAlign: "center", paddingBottom: 40, borderBottom: `1px solid ${t.border}`, marginBottom: 40 }}>
        <div style={{ display: "inline-flex", alignItems: "center", gap: 8, marginBottom: 18 }}>
          <span style={{ width: 28, height: 1, background: t.accent, opacity: 0.5, display: "inline-block" }} />
          <span style={{ fontFamily: "'Syne', sans-serif", fontSize: 11, fontWeight: 600, letterSpacing: "0.22em", textTransform: "uppercase", color: t.accent }}>AI MultiTool Studio</span>
          <span style={{ width: 28, height: 1, background: t.accent, opacity: 0.5, display: "inline-block" }} />
        </div>

        <h1 style={{ fontFamily: "'Syne', sans-serif", fontSize: "clamp(38px,6vw,64px)", fontWeight: 800, letterSpacing: "-0.025em", lineHeight: 1.08, marginBottom: 18 }}>
          Everything AI,{" "}
          <span style={{ background: `linear-gradient(135deg, ${t.accent}, ${t.accent2})`, WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>
            All Together
          </span>
        </h1>

        <p style={{ fontSize: 17, color: t.textSecondary, fontWeight: 300, lineHeight: 1.7, maxWidth: 500, margin: "0 auto 0" }}>
          One unified workspace for chatbots, image generation, document intelligence, and AI-powered content.
        </p>
      </div>

      {/* Stat strip */}
      <div style={{ display: "flex", border: `1px solid ${t.border}`, borderRadius: 14, overflow: "hidden", background: t.bgCard, marginBottom: 40 }}>
        {[["4", "AI Tools"], ["∞", "Possibilities"], ["1", "Workspace"], ["0", "Complexity"]].map(([n, l], i, arr) => (
          <div key={l} style={{ flex: 1, padding: "18px 0", textAlign: "center", borderRight: i < arr.length - 1 ? `1px solid ${t.border}` : "none" }}>
            <div style={{ fontFamily: "'Syne', sans-serif", fontSize: 22, fontWeight: 800, color: t.accent }}>{n}</div>
            <div style={{ fontSize: 10, color: t.textMuted, marginTop: 4, textTransform: "uppercase", letterSpacing: "0.08em", fontWeight: 500 }}>{l}</div>
          </div>
        ))}
      </div>

      {/* Tools */}
      <SectionHeader t={t} label="AI Tools" />
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14, marginBottom: 40 }}>
        {tools.map(tool => (
          <ToolCard key={tool.title} t={t} {...tool} />
        ))}
      </div>

      <div style={{ height: 1, background: `linear-gradient(90deg, transparent, ${t.border}, transparent)`, margin: "0 0 36px" }} />

      {/* Features */}
      <SectionHeader t={t} label="Why MultiGPT" />
      <div style={{ display: "flex", flexWrap: "wrap", gap: 10, marginBottom: 48 }}>
        {features.map(f => (
          <div key={f} style={{ background: t.bgCard, border: `1px solid ${t.border}`, borderRadius: 100, padding: "10px 20px", fontSize: 14, color: t.textPrimary, display: "flex", alignItems: "center", gap: 8 }}>
            <span style={{ width: 6, height: 6, borderRadius: "50%", background: t.accent, flexShrink: 0, display: "inline-block" }} />
            {f}
          </div>
        ))}
      </div>

      <div style={{ textAlign: "center", fontSize: 13, color: t.textMuted, letterSpacing: "0.05em", paddingTop: 16, borderTop: `1px solid ${t.border}` }}>
        Powered by AI &nbsp;·&nbsp; Built by <strong style={{ color: t.textSecondary, fontWeight: 500 }}>Azmi</strong> ❤️
      </div>
    </div>
  );
}

function InnerPage({ t, page, data }) {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  return (
    <div>
      {/* Page Hero */}
      <div style={{ paddingBottom: 28, borderBottom: `1px solid ${t.border}`, marginBottom: 32 }}>
        <div style={{ display: "inline-flex", alignItems: "center", gap: 6, background: t.badgeBg, color: t.accent2, fontFamily: "'Syne', sans-serif", fontSize: 11, fontWeight: 600, letterSpacing: "0.12em", textTransform: "uppercase", padding: "5px 14px", borderRadius: 100, marginBottom: 16 }}>
          ✦ {data.badge}
        </div>
        <h2 style={{ fontFamily: "'Syne', sans-serif", fontSize: "clamp(28px,4vw,44px)", fontWeight: 800, letterSpacing: "-0.02em", marginBottom: 10, lineHeight: 1.1 }}>
          {data.title}
        </h2>
        <p style={{ fontSize: 16, color: t.textSecondary, fontWeight: 300, lineHeight: 1.6, maxWidth: 520 }}>{data.sub}</p>
      </div>

      {/* Chips */}
      <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginBottom: 32 }}>
        {data.chips.map(c => (
          <div key={c} style={{ background: t.tagBg, border: `1px solid ${t.border}`, color: t.textSecondary, fontSize: 13, padding: "7px 16px", borderRadius: 100, display: "flex", alignItems: "center", gap: 6 }}>
            {c}
          </div>
        ))}
      </div>

      {/* Mock Input Area */}
      <div style={{ background: t.bgCard, border: `1px solid ${t.border}`, borderRadius: 14, padding: 24, marginBottom: 16 }}>
        <div style={{ fontFamily: "'Syne', sans-serif", fontSize: 11, fontWeight: 600, letterSpacing: "0.15em", textTransform: "uppercase", color: t.textMuted, marginBottom: 12 }}>
          {page === "Chatbot" ? "Your message" : page === "Image Generator" ? "Describe your image" : page === "Document QA" ? "Upload PDF & ask" : "Your topic"}
        </div>
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder={page === "Chatbot" ? "Ask me anything…" : page === "Image Generator" ? "A futuristic city at dusk, cinematic lighting…" : page === "Document QA" ? "What is the main topic of this document?" : "Benefits of AI in Education"}
          style={{ width: "100%", background: t.bgSecondary, border: `1px solid ${t.border}`, borderRadius: 10, padding: "12px 16px", color: t.textPrimary, fontSize: 15, outline: "none", fontFamily: "inherit" }}
        />
        <button
          onClick={() => setOutput(`This is a design preview — connect your Gemini API key in the Streamlit app to get real AI responses for "${input || "your input"}".`)}
          style={{ marginTop: 14, background: `linear-gradient(135deg, ${t.accent}, ${t.accent2})`, color: "#fff", border: "none", borderRadius: 10, padding: "10px 24px", fontFamily: "'Syne', sans-serif", fontWeight: 600, fontSize: 14, letterSpacing: "0.05em", cursor: "pointer" }}
        >
          ✦ {page === "Chatbot" ? "Send" : page === "Image Generator" ? "Generate" : page === "Document QA" ? "Ask AI" : "Generate Content"}
        </button>
      </div>

      {/* Output */}
      {output && (
        <div style={{ background: t.bgCard, border: `1px solid ${t.border}`, borderLeft: `3px solid ${t.accent}`, borderRadius: 12, padding: 24 }}>
          <div style={{ fontFamily: "'Syne', sans-serif", fontSize: 10, fontWeight: 700, letterSpacing: "0.18em", textTransform: "uppercase", color: t.accent, marginBottom: 10 }}>AI Output</div>
          <p style={{ fontSize: 15, color: t.textSecondary, lineHeight: 1.7, fontWeight: 300 }}>{output}</p>
        </div>
      )}

      <div style={{ textAlign: "center", fontSize: 13, color: t.textMuted, letterSpacing: "0.05em", marginTop: 48, paddingTop: 16, borderTop: `1px solid ${t.border}` }}>
        Powered by <strong style={{ color: t.textSecondary, fontWeight: 500 }}>Gemini 2.0 Flash Lite</strong> ✨
      </div>
    </div>
  );
}

function SectionHeader({ t, label }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 20 }}>
      <span style={{ fontFamily: "'Syne', sans-serif", fontSize: 12, fontWeight: 600, letterSpacing: "0.18em", textTransform: "uppercase", color: t.textMuted, whiteSpace: "nowrap" }}>{label}</span>
      <div style={{ flex: 1, height: 1, background: t.border }} />
    </div>
  );
}

function ToolCard({ t, icon, title, desc, tag }) {
  const [hovered, setHovered] = useState(false);
  return (
    <div
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      style={{
        background: hovered ? t.bgCardHover : t.bgCard,
        border: `1px solid ${hovered ? t.accent : t.border}`,
        borderRadius: 16, padding: "24px 22px",
        transition: "all 0.22s cubic-bezier(.4,0,.2,1)",
        transform: hovered ? "translateY(-2px)" : "none",
        boxShadow: hovered ? `0 0 0 1px ${t.accent}, 0 8px 32px ${t.accentGlow}` : "none",
        position: "relative", overflow: "hidden", cursor: "default",
      }}
    >
      <div style={{ position: "absolute", inset: 0, background: `linear-gradient(135deg, ${t.shine}, transparent 60%)`, pointerEvents: "none" }} />
      <div style={{ fontSize: 24, marginBottom: 10 }}>{icon}</div>
      <div style={{ fontFamily: "'Syne', sans-serif", fontSize: 16, fontWeight: 700, color: t.textPrimary, marginBottom: 7, letterSpacing: "-0.01em" }}>{title}</div>
      <div style={{ fontSize: 14, color: t.textSecondary, lineHeight: 1.6, fontWeight: 300 }}>{desc}</div>
      <div style={{ display: "inline-block", background: t.tagBg, color: t.accent, fontFamily: "'Syne', sans-serif", fontSize: 10, fontWeight: 600, letterSpacing: "0.1em", textTransform: "uppercase", padding: "3px 10px", borderRadius: 100, marginTop: 12 }}>{tag}</div>
    </div>
  );
}
