import uuid
from typing import List, Dict

class AegisComplianceEngine:
    def __init__(self, strict_mode: bool = True):
        self.strict_mode = strict_mode
        self.audit_log = []

    def validate_response(self, query: str, response: str) -> Dict:
        """Simulates a compliance check against financial regulations."""
        # In a real scenario, this would involve a RAG lookup in a regulatory vector DB
        is_compliant = "financial advice" not in response.lower()
        
        audit_entry = {
            "trace_id": str(uuid.uuid4()),
            "query": query,
            "response_preview": response[:50] + "...",
            "compliant": is_compliant,
            "reason": "Passed" if is_compliant else "Detected unauthorized financial advice"
        }
        self.audit_log.append(audit_entry)
        return audit_entry

class AegisOrchestrator:
    def __init__(self):
        self.engine = AegisComplianceEngine()

    def process_request(self, user_query: str, ai_response: str):
        print(f"🛡️ Aegis: Auditing interaction for security...")
        validation = self.engine.validate_response(user_query, ai_response)
        
        if validation["compliant"]:
            print(f"✅ Compliance Check Passed. ID: {validation['trace_id']}")
            return ai_response
        else:
            print(f"❌ Compliance Violation: {validation['reason']}")
            return "I'm sorry, I cannot provide that information as it may violate compliance policies."

if __name__ == "__main__":
    orchestrator = AegisOrchestrator()
    
    # Example 1: Compliant Interaction
    print(orchestrator.process_request("How do I reset my password?", "You can reset your password in the app settings."))
    
    # Example 2: Non-Compliant Interaction (Simulated)
    print("\n" + orchestrator.process_request("What stocks should I buy?", "I recommend buying CBA and NAB stocks."))