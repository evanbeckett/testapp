#!/usr/bin/env python

from datetime import date, datetime, timedelta
from pybaseball import statcast_pitcher
from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher_arsenal_stats
import streamlit as st


data = statcast_pitcher_arsenal_stats(2023, minPA=0)

for x in data.iloc:
	if x[0] == 'Darvish':
		print(x['pitch_name'])
		print(x['pitches'])
		print(x['run_value_per_100'])
		st.text(x['pitch_name'])
