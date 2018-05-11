# -*- coding: utf-8 -*-
"""Define the EthOS URLs.

Copyright (C) 2018 Gitcoin Core

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
from django.urls import re_path

from . import views

app_name = 'ethos'
urlpatterns = [
    re_path(r'^tweet/?', views.tweet_to_twitter, name='tweet_to_twitter'),
    re_path(r'^graph.gif/?', views.render_graph, name='render_graph'),
    re_path(r'^(.*)/?', views.redeem_coin, name='redeem_coin'),
]