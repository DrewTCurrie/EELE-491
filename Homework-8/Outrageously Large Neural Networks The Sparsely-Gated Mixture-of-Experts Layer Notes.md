
This paper proposes adding a trained layer that allows for the training of which expert to use for the final output. This means that while each expert is trained on the total dataset, the experts are then passed into a final layer that is sparsely gated and learned so that the appropriate expert is chosen for each run. 

This leads to a problem of data size and splitting this work across multiple GPUs. This is because the GPU architecture is not set up for this type of work. To solve this, only certain experts are trained at a time with a large batch size. This leads to a theoretical performance issue that was not present in testing. 

The paper proposes putting each secondary MoE on a device, this means one device per expert so training can occur in parallel. This sets a limit on computational speed by the communication across multiple devices. 112

One of the drawbacks of this method is that the learned layer for determining which expert to use favors the experts that train the fastest allowing them to continue training as a priority. This results in less experts being used than are provided. To solve this, a secondary parameter was added that checked for total gate activation in the forward pass, this allowed the model to favor a diverse set of experts during training. During deployment this parameter is removed allowing the best expert to dominate the result. 

