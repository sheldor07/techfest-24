## Why Vibes?

3 facts

-  WorldStream statistic's say 33.33% of all online activity is dedicated to video consumption.
- According to As of November 2023, there are over 200 million content creators worldwide.
- As of January 2024, there are 207 million content creators worldwide.

The truth is loud and clear, content is the present and future of consumption and content creators are leading this digital rennaisance. Yet, their creative freedom is often eclipsed by the shadow of restrictive copyright laws, especially in the realm of music. Vibes is our answer to this creative conundrum, a platform where technology meets imagination. Leveraging AI, Vibes empowers creators to compose bespoke, copyright-free music, ensuring their stories resonate authentically and their creativity flows, unbounded.

## What does Vibes do? **We Redefine the Creative Process**

1. **Tailored Creation**: For creators with a precise sound in mind, Vibes offers a streamlined process. Specify the **genre**, **duration**, and **mood**, and our platform delivers a custom, royalty-free soundtrack in minutes. Say goodbye to endless searching and hello to instant, perfect-fit music.

2. **Inspired Solutions**: Uncertain moments call for inspired solutions. Upload a screenshot of your video segment, and let Vibes’ **Multimodal AI** understand the context, offering an **audio backdrop** that elevates your content. It's not just music generation; it's a leap into a new realm of creative intuition.

3. **Community-Led Ecosystem**: Creation is a shared journey. Dive into Vibes' **public library** of royalty-free music, curated and used by **fellow creators**. Connect, collaborate, and grow together in a space where every track tells a story and every creator contributes to the collective narrative.

Vibes is more than a platform; it's a partner in your creative journey, ensuring your vision resonates with every note.


## How did we do it? 

**Frontend Sophistication**: The user interface of Vibes is crafted with React, ensuring a seamless and responsive experience for every creator.

**Backend Complexity**: 
[Pictoral Representation here](https://cdn.discordapp.com/attachments/424925407280758788/1204247777488539808/Screenshot_2024-02-06_at_10.10.37_AM.png?ex=65d40a23&is=65c19523&hm=f46935da17875ca244a72d413b4975f60725d164b7d6b9f334baf402fb86fc94&)
At its core, Vibes runs on a robust backend architecture:
1. **Django Server**: Powers our innovative image-to-text-to-speech, image-to-text-to-audio, and image-to-text-to-music functionalities, alongside our unique text-to-music models.
2. **AWS Lambda Functions**: Manage user authentication, posts management, and interaction with our **Postgres database** for a scalable and efficient infrastructure.
3. **State-of-the-Art Models**: Vibes leverages cutting-edge technology to revolutionize content creation:
	- _Meta's MusicGen_: Our backbone for audio generation, enhanced with a fine-tuned GPT for superior results, transcending the capabilities of MusicGen Vanilla.
		- Custom Deployment: A dedicated T4 GPU hosts our bespoke version of MusicGen on AWS through HuggingFace, offering unparalleled performance and creativity.
	- __Vision and Theme Generation__: GPT-4 Vision for precise image inputs and a fine-tuned GPT for generating immersive themes and genres, setting a new standard in content creation synergy.

## It was not easy.
- Ideation in a Competitive Landscape: Breaking new ground in generative AI, where **every conceivable solution seems already claimed by heavily funded entities**, posed a significant creative challenge. Ideating a unique value proposition for Vibes demanded **deep market insights and inventive thinking**.

- Resource Scarcity and Innovation: Securing a GPU amidst a market shortage required ingenuity. We embraced this challenge by leveraging Hugging Face, creating a **custom handler for our MusicGen instance** to ensure precise **tensor outputs**, seamlessly convertible into wav files.

- Architectural Adaptability: Our vision of a completely serverless architecture met with the **limitations of Lambda functions**, notably their 30-second timeout. Adapting swiftly, we engineered a **Django server on EC2**, an improvisation executed merely six hours before submission, showcasing our team's agility and technical acumen.

## Accomplishments that we're proud of

Our crowning achievement lies in transforming Vibes from concept to reality, crafting a fully functional product without "hacks". The collaborative synergy between just two minds not only powered us through challenges but also resulted in a robust platform, ready to transcend the hackathon and make a lasting impact in the real world.

## What's next for Vibes

Testing with real users, Iterating and maybe even making a billion dolalrs
