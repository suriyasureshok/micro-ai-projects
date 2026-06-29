from pydantic_ai import RunContext

from models import UserSession


def get_username(ctx: RunContext[UserSession]) -> str:
    """
    Returns the username of the current user.
    """
    return ctx.deps.username


def get_account_type(ctx: RunContext[UserSession]) -> str:
    """
    Returns the account type of the current user.
    """
    return ctx.deps.account_type


def get_balance(ctx: RunContext[UserSession]) -> float:
    """
    Returns the current account balance.
    """
    return ctx.deps.balance
