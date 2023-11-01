from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
import os

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

def generate_linkedin_message(connection, myname,name, position, company):
    llm = OpenAI(temperature=0.6)

    prompt_template_name = PromptTemplate(
        input_variables=['connection','myname','name', 'position','company'],
        template="""My name is {myname}. I'm looking to connect with {name}, who is working as a {position} at {company}. He or she is a {connection}, make sure to write
        accordingly. Write me a short and precise introductory linkedin message asking to connect and request a coffee chat. Make it a little bit casual and personal.
        Express interest in the field and industry. Make it more cheerful! Limit to 300 characters.
        """
    )
    name_chain = LLMChain(llm=llm, prompt = prompt_template_name,output_key="linkedin_message")
    
    response  = name_chain({'connection':connection, 'myname': myname, 'name': name, 'position': position, 'company' : company})
    return response


if __name__ == "__main__":
    print (generate_linkedin_message("James", "Jordan", "Data Analyst", "Netomi"))