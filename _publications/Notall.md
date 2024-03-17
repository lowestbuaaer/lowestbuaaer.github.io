---
title: "Not All Steps are Equal: Efficient Generation with Progressive Diffusion Models"
collection: publications
permalink: /publication/Notall
excerpt: 'Diffusion models have demonstrated remarkable efficacy in various generative tasks with the predictive prowess of denoising model. Currently, these models employ a uniform denoising approach across all timesteps. However, the inherent variations in noisy latents at each timestep lead to conflicts during training, constraining the potential of diffusion models. To address this challenge, we propose a novel two-stage training strategy termed Step-Adaptive Training. In the initial stage, a base denoising model is trained to encompass all timesteps. Subsequently, we partition the timesteps into distinct groups, fine-tuning the model within each group to achieve specialized denoising capabilities. Recognizing that the difficulties of predicting noise at different timesteps vary, we introduce a diverse model size requirement. We dynamically adjust the model size for each timestep by estimating task difficulty based on its signal-to-noise ratio before fine-tuning. This adjustment is facilitated by a proxy-based structural importance assessment mechanism, enabling precise and efficient pruning of the base denoising model. Our experiments validate the effectiveness of the proposed training strategy, demonstrating an improvement in the FID score on CIFAR10 by over 0.3 while utilizing only 80% of the computational resources. This innovative approach not only enhances model performance but also significantly reduces computational costs, opening new avenues for the development and application of diffusion models.'
date: 2024-02-15
venue: 'CVPR'
paperurl: 'https://arxiv.org/html/2312.13307v2'
citation: 'Li W, Su X, You S, et al. Not All Steps are Equal: Efficient Generation with Progressive Diffusion Models[J]. arXiv preprint arXiv:2312.13307, 2023.'
---

The contents above will be part of a list of publications, if the user clicks the link for the publication than the contents of section will be rendered as a full page, allowing you to provide more information about the paper for the reader. When publications are displayed as a single page, the contents of the above "citation" field will automatically be included below this section in a smaller font.
