# Try openai

The repo is my practice playground for learning openai api.
when using each py file, be careful about the rate limit policy from openai.

## environment

I use python3 (v3.9.13) and pip3 (v23.1.2)

```
pip3 install load_dotenv
pip3 install openai
```

## Resources

* [best strategies](https://platform.openai.com/docs/guides/gpt-best-practices/six-strategies-for-getting-better-results)
* [usage example](https://platform.openai.com/examples)
* [LEARN GENERATIVE AI Short Courses in https://www.deeplearning.ai](https://www.deeplearning.ai/short-courses/)


## Learning Notes:

1. `Chat completions` vs `Completions`?

- Completions takes a single string as input, however chat completions is given dialog and response the result with specfic format.
- chat completions using a list of messages; completions use a freeform text string called prompt.

2. role system vs assistant vs user

- system -> used to guide the assistant's behavior or tone, e.g.:

```js
{'role':'system', 'content': 'You are an assistant that speaks like Shakespeare.'}
{'role':'system', 'content': 'You are a helpful assistant.'}
{'role':'system', 'content': 'All your response must use emoji'}
```

- assistant -> LLM response
- user -> prompt