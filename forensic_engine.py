import os
import json
import requests

# This engine uses the Google Gemini API to generate content
# It follows the 'Forensic' style constraints

API_KEY = os.getenv("GOOGLE_API_KEY") # We assume this is set

def generate_forensic_post(question):
    print(f"Generating forensic post for: {question}")
    
    # SYSTEM PROMPT
    system_prompt = """
    You are an elite Security & Connectivity Engineer (Gary Pearce). 
    Your style is 'Forensic SEO' (Julian Goldie strategy).
    
    CONSTRAINTS:
    1. STRICT 2-3 sentences per paragraph.
    2. Use professional, technical language (bitrate, encryption, firmware, cat7, WiFi 7, NVR, DVR, Ajax, Hikvision).
    3. Format in PURE HTML (h2, h3, p, ul, li). No markdown.
    4. Mention Gary Pearce Home Services (07830638337) and North East England coverage.
    5. Be authoritative and forensic in your analysis.
    """
    
    user_prompt = f"Write a deep-dive technical blog post answering: {question}"
    
    # Since I am the agent, I will generate a template content here
    # In the final version, this would be a real API call.
    
    content = f"""
    <h2>Forensic Security Audit: {question}</h2>
    <p>In the rapidly evolving landscape of 2026, the question of {question} has become a focal point for security-conscious homeowners and businesses alike.</p>
    <p>We approach this from a forensic engineering perspective, analyzing the hardware capabilities and software integration of leading brands like Ajax and Hikvision.</p>
    
    <h3>Technical Hardware Breakdown</h3>
    <p>When assessing system reliability, we focus on the redundancy of signal transmission and the encryption standards applied at the firmware level.</p>
    <ul>
        <li><strong>Military-Grade AES Encryption:</strong> Ensuring that all data streams are protected from interception or tampering.</li>
        <li><strong>Multi-Channel Redundancy:</strong> Using both GSM, Ethernet, and WiFi 7 to ensure constant connectivity even in rural areas.</li>
        <li><strong>Forensic Imaging:</strong> High-bitrate 8K sensors provide court-admissible evidence that standard consumer cameras miss.</li>
    </ul>
    
    <h3>Local Implementation Excellence</h3>
    <p>Gary Pearce Home Services specializes in deploying these high-end solutions across Newcastle, Durham, and Northumberland, ensuring full compliance with UK GDPR and surveillance laws.</p>
    <p>We don't just install hardware; we engineer a security ecosystem that provides peace of mind and bulletproof evidence when it matters most.</p>
    
    <h3>Actionable Professional Insight</h3>
    <p>If you are considering a security upgrade in 2026, prioritize systems with active deterrence and cloud-agnostic local storage options to minimize latency and maximize privacy.</p>
    <p>For a bespoke forensic security consultation, contact Gary Pearce directly to discuss your specific requirements and environment.</p>
    """
    
    return content

if __name__ == "__main__":
    # Test
    print(generate_forensic_post("Is the Ajax alarm system unhackable?"))
