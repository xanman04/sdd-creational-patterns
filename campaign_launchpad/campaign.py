
from dataclasses import dataclass
from datetime import date
from typing import Optional, Dict, Any, List


@dataclass(frozen=True)
class Campaign:
    name: str
    channel: str
    daily_budget: float
    start_date: date
    end_date: Optional[date]
    target_audience: Dict[str, Any]
    creatives: List[Dict[str, str]]
    tracking: Dict[str, str]


class CampaignBuilder:
    def __init__(self):
      self.name = ""
      self.channel = ""
      self.daily_budget = 0.0
      self.start_date: date
      self.end_date: Optional[date]
      self.target_audience = {}
      self.creatives = []
      self.tracking = {}

    def with_name(self, name: str):
      self.name = name
      return self

    def with_channel(self, channel: str):
      self.channel = channel
      return self

    def with_budget(self, daily_budget: float):
      self.daily_budget = daily_budget
      return self

    def with_dates(self, start_date, end_date):
      self.start_date = start_date
      self.end_date = end_date
      return self

    def with_audience(self, **kwargs):
      for arg in kwargs:
        self.target_audience.update(kwargs)
      return self

    def add_creative(self, headline: str, image_url: str):
      self.creatives = [{headline : image_url}]
      return self

    def with_tracking(self, **kwargs):
      self.tracking.update(kwargs)
      return self

    def build(self) -> Campaign:
      campaign = Campaign(
        self.name, 
        self.channel, 
        self.daily_budget, 
        self.start_date, 
        self.end_date,
        self.target_audience, 
        self.creatives, 
        self.tracking
        )

      if not campaign.name:
        raise ValueError("name")
      if not campaign.channel:
        raise ValueError("channel")
      if not campaign.daily_budget or campaign.daily_budget < 0:
        raise ValueError("budget")
      if not campaign.start_date or (campaign.end_date and campaign.end_date < campaign.start_date):
        raise ValueError("start date")
      if not campaign.creatives:
        raise ValueError("creatives")

      return campaign
