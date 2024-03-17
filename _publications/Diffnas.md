---
title: "DiffNAS: Bootstrapping Diffusion Models by Prompting for Better Architectures"
collection: publications
permalink: /publication/Diffnas
excerpt: 'Diffusion models have recently exhibited remarkable performance on synthetic data. After a diffusion path is selected, a base model, such as UNet, operates as a denoising autoencoder, primarily predicting noises that need to be eliminated step by step. Consequently, it is crucial to employ a model that aligns with the expected budgets to facilitate superior synthetic performance. In this paper, we meticulously analyze the diffusion model and engineer a base model search approach, denoted "DiffNAS". Specifically, we leverage GPT-4 as a supernet to expedite the search, supplemented with a search memory to enhance the results. Moreover, we employ RFID as a proxy to promptly rank the experimental outcomes produced by GPT-4. We also adopt a rapid-convergence training strategy to boost search efficiency. Rigorous experimentation corroborates that our algorithm can augment the search efficiency by 2× under GPT-based scenarios, while also attaining a performance of 2.82 with 0.37 improvement in FID on CIFAR10 relative to the benchmark IDDPM algorithm.'
date: 2023-10-07
venue: 'ICDM'
paperurl: 'https://ieeexplore.ieee.org/abstract/document/10415684'
citation: 'Li W, Su X, You S, et al. Diffnas: Bootstrapping diffusion models by prompting for better architectures[C]//2023 IEEE International Conference on Data Mining (ICDM). IEEE, 2023: 1121-1126.'
---

The contents above will be part of a list of publications, if the user clicks the link for the publication than the contents of section will be rendered as a full page, allowing you to provide more information about the paper for the reader. When publications are displayed as a single page, the contents of the above "citation" field will automatically be included below this section in a smaller font.
