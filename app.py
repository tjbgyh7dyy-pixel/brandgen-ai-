import streamlit as st

st.set_page_config(page_title="BrandGen AI (Lite)", page_icon="🤖", layout="centered")

st.title("🤖 BrandGen AI (Lite)")
st.write("Typ je business-idee en krijg meteen een mini brand kit (naam, tagline, kleuren, hero-tekst).")

idea = st.text_input("Beschrijf je business-idee")

def make_brand(idea: str):
    idea = (idea or "").strip()
    if not idea:
        return None
    brand_name = idea.title().replace(" ", "")
    tagline = "Launch in minutes, not months."
    colors = ["#0EA5E9 (blue-500)", "#111827 (slate-900)", "#F59E0B (amber-500)"]
    hero = f"Build your {idea} brand in minutes with AI."
    bullets = [
        f"Brand name: {brand_name}",
        f"Tagline: {tagline}",
        f"Colors: {', '.join(colors)}",
        f"Hero copy: {hero}",
    ]
    return bullets

if st.button("Generate"):
    out = make_brand(idea)
    if not out:
        st.warning("Vul eerst je idee in.")
    else:
        st.success("Mini brand kit")
        for b in out:
            st.write("• " + b)
