from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

from transformers import AutoTokenizer
import transformers
import torch


def instantiate_llm():
  model = "meta-llama/Llama-2-7b-chat-hf" # https://huggingface.co/meta-llama/Llama-2-70b-chat-hf
  # model = "meta-llama/Meta-Llama-3-8B" # https://huggingface.co/meta-llama/Meta-Llama-3-8B

  tokenizer = AutoTokenizer.from_pretrained(model) # Fetch model config.json from HuggingFace and tokenize input text with that

  # Tool for generating text
  pipeline = transformers.pipeline(
      "text-generation", 
      model=model,
      tokenizer=tokenizer,
      torch_dtype=torch.bfloat16, # Use bfloat16 for faster inference
      trust_remote_code=True,
      truncation=True,
      device_map="auto", # Use GPU if available
      max_length=1000,
      eos_token_id=tokenizer.eos_token_id # End of sentence token
  )

  return HuggingFacePipeline(pipeline = pipeline, model_kwargs = {'temperature':0})


def construct_base_prompt():
  template = """
              You are an intelligent chatbot that gives out useful information to humans.
              Answer the following question in exactly 3 sentences.
              {query}
            """

  prompt = PromptTemplate(template=template, input_variables=["query"])
  # print((prompt | llm).invoke("What is the purpose of a large language model?"))
  return prompt