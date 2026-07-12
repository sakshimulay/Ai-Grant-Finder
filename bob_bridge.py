from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="IBM Bob Execution Bridge")

# Define the incoming data structure to match your OpenAPI file
class ProposalPayload(BaseModel):
    proposal_text: str

@app.post("/validate")
async def validate_proposal(payload: ProposalPayload):
    """
    Receives data payload from watsonx Orchestrate,
    checks structure syntax, and logs status in IBM Bob runtime.
    """
    print("\n[IBM Bob Engine] Payload received from watsonx Orchestrate successfully!")
    print(f"[Content Length]: {len(payload.proposal_text)} characters.")
    
    # Simple compilation validation check
    if "# Executive Summary" in payload.proposal_text:
        return {"status": "Verified: Layout Compliance Passed", "code": 200}
    else:
        return {"status": "Warning: Formatting Anomalies Detected", "code": 422}

if __name__ == "__main__":
    # Start the server on port 8000 to listen to the API link
    uvicorn.run(app, host="0.0.0.0", port=8000)