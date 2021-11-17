import torch
import torch.nn as nn
import torch.nn.functional as F


class WeightedBinaryCELoss(nn.Module):
    def __init__(self, temperature=100.0):
        nn.Module.__init__(self)
        self.temperature = temperature

    def forward(self, pos_score, neg_score, probs):
        weight = F.softmax(neg_score / self.temperature, -1)
        loss = -F.logsigmoid(pos_score.squeeze()) + torch.sum(F.softplus(neg_score) * weight, dim=-1)
        return loss