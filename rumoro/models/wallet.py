from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wallet_currency import WalletCurrency

if TYPE_CHECKING:
    from ..models.wallet_auto_recharge import WalletAutoRecharge
    from ..models.wallet_signup_credit_type_0 import WalletSignupCreditType0


T = TypeVar("T", bound="Wallet")


@_attrs_define
class Wallet:
    """
    Attributes:
        balance_cents (int): The ledger balance, all credits minus all settled debits.
        pending_cents (int): Cost of mentions matched after the last daily settlement. Not debited yet.
        effective_balance_cents (int): balanceCents minus pendingCents. Pausing at zero and the check before adding
            keywords both use this number.
        burn_per_day_cents (int): Mean daily debit across the past 7 days, or the workspace's lifetime if shorter.
        days_left (int | None): effectiveBalanceCents over burnPerDayCents, rounded down. Null when burnPerDayCents is
            0.
        stopped (bool): True when tracking is paused because the balance ran out. It resumes after a top-up that covers
            one day of every keyword.
        low_balance (bool): True when tracking is running and the effective balance is 20 percent of the last credit or
            less. The low-balance email uses the same rule.
        active_keywords (int): Keywords that are not muted.
        auto_muted_keywords (int): Keywords muted for low balance. A top-up restarts them.
        next_day_cents (int): Next day's cost for the running keywords. Tracking stops if the effective balance drops
            below it.
        resume_cost_cents (int): Daily cost of every keyword, running or paused. Tracking restarts once the effective
            balance reaches this amount.
        signup_credit (None | WalletSignupCreditType0): Welcome credit given to this workspace. Null when the user
            already got it in another workspace.
        last_top_up_at (None | str): Latest paid top-up time, or null if there is none.
        billing_configured (bool): Whether top-ups work here. false when Polar isn't configured, which hides the top-up
            button.
        min_top_up_cents (int): The minimum top-up at checkout.
        max_top_up_cents (int): The maximum for one top-up.
        default_top_up_cents (int): The amount the checkout starts with.
        currency (WalletCurrency): All amounts here are in US cents.
        auto_recharge (WalletAutoRecharge):
    """

    balance_cents: int
    pending_cents: int
    effective_balance_cents: int
    burn_per_day_cents: int
    days_left: int | None
    stopped: bool
    low_balance: bool
    active_keywords: int
    auto_muted_keywords: int
    next_day_cents: int
    resume_cost_cents: int
    signup_credit: None | WalletSignupCreditType0
    last_top_up_at: None | str
    billing_configured: bool
    min_top_up_cents: int
    max_top_up_cents: int
    default_top_up_cents: int
    currency: WalletCurrency
    auto_recharge: WalletAutoRecharge
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wallet_signup_credit_type_0 import WalletSignupCreditType0

        balance_cents = self.balance_cents

        pending_cents = self.pending_cents

        effective_balance_cents = self.effective_balance_cents

        burn_per_day_cents = self.burn_per_day_cents

        days_left: int | None
        days_left = self.days_left

        stopped = self.stopped

        low_balance = self.low_balance

        active_keywords = self.active_keywords

        auto_muted_keywords = self.auto_muted_keywords

        next_day_cents = self.next_day_cents

        resume_cost_cents = self.resume_cost_cents

        signup_credit: dict[str, Any] | None
        if isinstance(self.signup_credit, WalletSignupCreditType0):
            signup_credit = self.signup_credit.to_dict()
        else:
            signup_credit = self.signup_credit

        last_top_up_at: None | str
        last_top_up_at = self.last_top_up_at

        billing_configured = self.billing_configured

        min_top_up_cents = self.min_top_up_cents

        max_top_up_cents = self.max_top_up_cents

        default_top_up_cents = self.default_top_up_cents

        currency = self.currency.value

        auto_recharge = self.auto_recharge.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balanceCents": balance_cents,
                "pendingCents": pending_cents,
                "effectiveBalanceCents": effective_balance_cents,
                "burnPerDayCents": burn_per_day_cents,
                "daysLeft": days_left,
                "stopped": stopped,
                "lowBalance": low_balance,
                "activeKeywords": active_keywords,
                "autoMutedKeywords": auto_muted_keywords,
                "nextDayCents": next_day_cents,
                "resumeCostCents": resume_cost_cents,
                "signupCredit": signup_credit,
                "lastTopUpAt": last_top_up_at,
                "billingConfigured": billing_configured,
                "minTopUpCents": min_top_up_cents,
                "maxTopUpCents": max_top_up_cents,
                "defaultTopUpCents": default_top_up_cents,
                "currency": currency,
                "autoRecharge": auto_recharge,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wallet_auto_recharge import WalletAutoRecharge
        from ..models.wallet_signup_credit_type_0 import (
            WalletSignupCreditType0,
        )

        d = dict(src_dict)
        balance_cents = d.pop("balanceCents")

        pending_cents = d.pop("pendingCents")

        effective_balance_cents = d.pop("effectiveBalanceCents")

        burn_per_day_cents = d.pop("burnPerDayCents")

        def _parse_days_left(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_left = _parse_days_left(d.pop("daysLeft"))

        stopped = d.pop("stopped")

        low_balance = d.pop("lowBalance")

        active_keywords = d.pop("activeKeywords")

        auto_muted_keywords = d.pop("autoMutedKeywords")

        next_day_cents = d.pop("nextDayCents")

        resume_cost_cents = d.pop("resumeCostCents")

        def _parse_signup_credit(data: object) -> None | WalletSignupCreditType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                signup_credit_type_0 = WalletSignupCreditType0.from_dict(data)

                return signup_credit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WalletSignupCreditType0, data)

        signup_credit = _parse_signup_credit(d.pop("signupCredit"))

        def _parse_last_top_up_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_top_up_at = _parse_last_top_up_at(d.pop("lastTopUpAt"))

        billing_configured = d.pop("billingConfigured")

        min_top_up_cents = d.pop("minTopUpCents")

        max_top_up_cents = d.pop("maxTopUpCents")

        default_top_up_cents = d.pop("defaultTopUpCents")

        currency = WalletCurrency(d.pop("currency"))

        auto_recharge = WalletAutoRecharge.from_dict(d.pop("autoRecharge"))

        wallet = cls(
            balance_cents=balance_cents,
            pending_cents=pending_cents,
            effective_balance_cents=effective_balance_cents,
            burn_per_day_cents=burn_per_day_cents,
            days_left=days_left,
            stopped=stopped,
            low_balance=low_balance,
            active_keywords=active_keywords,
            auto_muted_keywords=auto_muted_keywords,
            next_day_cents=next_day_cents,
            resume_cost_cents=resume_cost_cents,
            signup_credit=signup_credit,
            last_top_up_at=last_top_up_at,
            billing_configured=billing_configured,
            min_top_up_cents=min_top_up_cents,
            max_top_up_cents=max_top_up_cents,
            default_top_up_cents=default_top_up_cents,
            currency=currency,
            auto_recharge=auto_recharge,
        )

        wallet.additional_properties = d
        return wallet

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
