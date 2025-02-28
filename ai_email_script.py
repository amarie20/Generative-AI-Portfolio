import openai
import json

def generate_email(subject_context, recipient_name, company_name, pain_point, cta):
    prompt = f"""
    Write a personalized email for a B2B SaaS company targeting {company_name}. The email should address {recipient_name} by name, mention their pain point: '{pain_point}', and include a strong call to action: '{cta}'. Keep it professional yet conversational.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a marketing AI assistant."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# Example Usage
subject = "Optimizing Your Workflow Efficiency"
recipient = "John Doe"
company = "Tech Solutions Inc."
pain_point = "Reducing manual reporting time"
cta = "Let’s schedule a quick 15-minute call next week."

email_content = generate_email(subject, recipient, company, pain_point, cta)
print(email_content)
