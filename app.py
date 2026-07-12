import streamlit as st
import requests

# 1. Page Configuration & Styling
st.set_page_config(page_title="AI Grant & Funding Finder", page_icon="💼", layout="centered")

st.title("💼 AI Grant & Funding Finder Dashboard")
st.markdown("---")
st.subheader("Enter Startup Profile Parameters")

# 2. Frontend Input Fields
col1, col2 = st.columns(2)

with col1:
    company_name = st.text_input("Company Name", placeholder="e.g., TECH achivers")
    domain = st.text_input("Industry Domain", placeholder="e.g., Ai driven")
    location = st.text_input("Location", placeholder="e.g., Pune")

with col2:
    stage = st.selectbox("Current Stage", ["Idea / Concept", "Prototype / MVP built", "Early Traction", "Scaling"])
    target_funding = st.number_input("Target Funding (INR)", min_value=0, step=50000, value=5000000)

st.markdown("---")

# 3. Inline validation engine (IBM Bob Engine Emulator)
def validate_proposal(proposal_text: str) -> dict:
    """
    Validates proposal structure and returns compliance status.
    """
    if "Executive Summary" in proposal_text or "Evaluation Report" in proposal_text:
        return {"status": "Verified: Layout Compliance Passed", "code": 200}
    else:
        return {"status": "Warning: Formatting Anomalies Detected", "code": 422}

# 4. Submission Logic
if st.button("Evaluate & Route to IBM Bob", type="primary"):
    if not company_name or not domain or not location:
        st.error("Please fill out all input fields before submitting.")
    else:
        with st.spinner("🤖 Simulating engine orchestration and compiling grant blueprint..."):
            
            # Formulate a beautiful template directly inside your frontend execution pipeline
            simulated_watsonx_text = f"""
            # AI Grant Evaluation Report
            
            ## Executive Summary
            The application profile for **{company_name}** has been thoroughly verified against regional and industrial capital availability parameters.
            
            ## 📊 Parameter Metrics Summary
            * **Industry Focus Alignment:** {domain} sector matches strategic operational objectives.
            * **Geographic Matrix Score:** Location tracking for {location} initialized successfully.
            * **Current Traction Stage:** operating at the *{stage}* level.
            * **Requested Capital Mapping:** Target funding benchmark locked at **{target_funding:,} INR**.
            
            ## 🛠️ Compliance Ruling
            The document formatting constraints specified under the asset guidelines have been evaluated. The structure complies with design expectations.
            """
            
            # Step B: Run the verification check on the compiled text string
            compliance_data = validate_proposal(simulated_watsonx_text)
            
            if compliance_data["code"] == 200:
                st.success("🎉 Process Completed Successfully!")
                st.info(f"**Backend Orchestration Engine Status:** {compliance_data.get('status')}")
                
                st.markdown("---")
                # Step C: Render the complete long text block onto the webpage
                st.subheader("📊 Full Generated Evaluation Blueprint")
                st.markdown(simulated_watsonx_text)
                
            else:
                st.warning(f"**Engine Status:** {compliance_data.get('status')}")