# -*- coding: utf-8 -*-


def get_rnn_hidden_state(h):
    """Returns h_t transparently regardless of RNN type."""
    return h if not isinstance(h, tuple) else h[0]


def mean_pool(data):
    """Simple mean pool function for transforming 3D features of shape
    [T]imesteps x [B]atch_size x [F]eature_size into 2D BxF features.
    (author: @klmulligan)

        Arguments:
            data (tuple): Encoder result of form (data: Tensor(TxBxF), mask: Tensor(TxB))
        Returns:
            pooled_data (Tensor): Mean pooled data of shape BxF.
    """
    # Unpack
    x, mask = data

    if mask is not None:
        return x.sum(0) / mask.sum(0).unsqueeze(1)
    else:
        return x.mean(0)
