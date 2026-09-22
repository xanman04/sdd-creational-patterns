
from abc import ABC, abstractmethod
from uuid import uuid4
from .budget import GlobalBudget
from .campaign import Campaign
from random import randint


class ChannelClient(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> str:
      ...

    @abstractmethod
    def pause_campaign(self, campaign_id: str) -> None:
      pass


class GoogleAdsClient(ChannelClient):
  def create_campaign(self, campaign: Campaign) -> str:
    GlobalBudget().allocate(amount=campaign.daily_budget)
    return f"g-{randint(1000, 9999)}"
  def pause_campaign(self, campaign_id: str) -> None:
    return super().pause_campaign(campaign_id)

class FacebookAdsClient(ChannelClient):
  def create_campaign(self, campaign: Campaign) -> str:
    GlobalBudget().allocate(amount=campaign.daily_budget)
    return f"f-{randint(1000, 9999)}"
  def pause_campaign(self, campaign_id: str) -> None:
    return super().pause_campaign(campaign_id)

class ChannelClientFactory:
  @staticmethod
  def create(channel: str) -> ChannelClient:
    factory_map = {
      "google": GoogleAdsClient,
      "facebook": FacebookAdsClient
    }
    if channel not in factory_map:
      raise ValueError(f"Unknown channel: {channel}")

    return factory_map[channel](name=channel)