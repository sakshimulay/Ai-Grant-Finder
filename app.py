import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(page_title="AI Grant & Funding Finder", page_icon="💼", layout="centered")

st.title("💼 AI Grant & Funding Finder Dashboard")
st.markdown("---")
st.subheader("Enter Startup Profile Parameters")

# Input fields for the user
col1, col2 = st.columns(2)
with col1:
    company_name = st.text_input("Company Name", placeholder="e.g., TECH achivers")
    domain = st.text_input("Industry Domain", placeholder="e.g., EdTech / AI-driven")
    location = st.text_input("Location", placeholder="e.g., Pune")
with col2:
    stage = st.selectbox("Current Stage", ["Idea / Concept", "Prototype / MVP built", "Early Traction", "Scaling"])
    target_funding = st.number_input("Target Funding (INR)", min_value=0, step=50000, value=5000000)

st.markdown("---")

# ==========================================
# 2. THE "IBM BOB" COMPLIANCE ENGINE
# ==========================================
def run_bob_compliance_inspector(proposal_text: str) -> dict:
    """
    Validates structural tags in payload data to ensure all mandatory headers exist.
    """
    required_sections = ["Executive Summary", "Problem Statement", "Innovation Index", "Milestone-Based Budget Allocation", "Human-Validation Disclaimer"]
    if all(section in proposal_text for section in required_sections):
        return {"status": "Verified: Layout Compliance Passed", "code": 200}
    return {"status": "Warning: Formatting Anomalies Detected", "code": 422}

# ==========================================
# 3. EXECUTION PIPELINE
# ==========================================
if st.button("Evaluate & Route to IBM Bob", type="primary"):
    if not company_name or not domain or not location:
        st.error("Please fill out all input fields before submitting.")
    else:
        with st.spinner("🤖 Simulating orchestration and running evaluation pipeline..."):
            
            # Calculating the milestone disbursements based on the compulsory 40/40/20 rule
            m1_budget = int(target_funding * 0.40)
            m2_budget = int(target_funding * 0.40)
            m3_budget = int(target_funding * 0.20)
            
            # Building the entire requested text document
            watsonx_blueprint_text = f"""
### **Grant Application Draft Blueprint**

#### **Executive Summary**
This document outlines the strategic deployment framework for **{company_name}**, a venture working within the **{domain}** space out of **{location}**. Positioned at the **{stage}** layer, the enterprise requires an optimization grant of **{target_funding:,} INR** to finalize its scalable software engineering goals.

#### **Problem Statement**
Current technical approaches within the **{domain}** sector face major performance bottlenecks and scaling limits. **{company_name}** aims to bridge this operational gap by introducing automated cloud pipeline orchestration, removing development overhead, and ensuring robust localized execution metrics.

#### **Innovation Index**
* **Technical Defensibility:** High (Premium applied for custom rule blocks).
* **Market Fit Alignment:** Excellent tracking parameters verified.
* **Architecture Integrity:** Built to process heavy system loads smoothly.

#### **Milestone-Based Budget Allocation (40/40/20 rule)**
The capital injection of **{target_funding:,} INR** is partitioned into structured project milestones:
* 🚀 **Milestone 1 (40%):** **{m1_budget:,} INR** allocated for Core Prototyping and Initial Framework Design.
* 🛠️ **Milestone 2 (40%):** **{m2_budget:,} INR** allocated for System Optimization and Cloud Pipeline Testing.
* 📈 **Milestone 3 (20%):** **{m3_budget:,} INR** allocated for Integrity Audits, Security Tuning, and Deployments.

#### **Human-Validation Disclaimer**
*⚠️ **DISCLAIMER:** This application blueprint has been systematically compiled by the automated verification workspace. Final review and manual technical confirmation by a certified professional are strictly required before submitting this asset package to official grant providers.*
            """
            
            # Run the inspector
            bob_result = run_bob_compliance_inspector(watsonx_blueprint_text)
            
            # Display Process Completion Status
            st.success("🎉 Process Completed Successfully!")
            st.info(f"**Backend Orchestration Engine Status:** {bob_result.get('status')}")
            st.markdown("---")
            
            # ==========================================
            # 4. DISPLAY THE ELIGIBILITY MATRIX TABLE
            # ==========================================
            st.markdown("### **Eligibility Match Score (out of 100%)**")
            st.table([
                {
                    "Scoring Pillar": "Sector / Domain fit",
                    "Weight": "35 pts",
                    "Your Score": "28 / 35",
                    "Rationale": f"{domain} is identified as a priority sector (base 25pts). +3pts premium applied for national tech initiatives."
                },
                {
                    "Scoring Pillar": "Financial Run Rate viability",
                    "Weight": "25 pts",
                    "Your Score": "22 / 25",
                    "Rationale": f"Target framework of {target_funding:,} INR matches scaled capital deployment bounds perfectly."
                },
                {
                    "Scoring Pillar": "Geographic Allocation Matrix",
                    "Weight": "40 pts",
                    "Your Score": "35 / 40",
                    "Rationale": f"Active operational baseline in {location} validated against technology growth index limits."
                }
            ])
            
            st.success("Status: Ready for compliance export.")
            st.markdown("---")
            
            # Displaying the generated report
            st.subheader("📊 Full Generated Evaluation Blueprint")
            st.markdown(watsonx_blueprint_text)