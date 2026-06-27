from pydantic_ai import RunContext


def calculate_tax(ctx: RunContext, income: float) -> float:
    """
    Calculates income tax at a flat 18%.

    Args:
        income: Annual income.

    Returns:
        Calculated tax amount.
    """
    return income * 0.18


def calculate_gst(ctx: RunContext, amount: float) -> float:
    """
    Calculates GST at a flat 18%.

    Args:
        amount: Product amount.

    Returns:
        GST amount.
    """
    return amount * 0.18
