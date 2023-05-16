WEBSITE_LIST = [{"https://www.youtube.com/":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "login-page":   'direct-link;signin',
                  "video":  'css selector;ytd-rich-item-renderer'
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{"trending":'relies_prev:partial link text;Trending',
                                   "music":   'relies_prev:partial link text;Music',
                                   "gaming":  'relies_prev:partial link text;Gaming',
                                   "news":    'relies_prev:partial link text;News',
                                   "sports":  'relies_prev:partial link text;Sports',
                                   "learning":'relies_prev:partial link text;Learning'
                                   },
                      "trending":{"video":'rand_ind:css selector;ytd-video-renderer'
                                  },
                      "music":{"video":'rand_ind:css selector;ytd-video-renderer'
                               },
                      "gaming":{"video":"rand_ind:css selector;ytd-video-renderer"
                          
                      },
                  }
                 }
                }, 
                {"https://ladbible.com":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:partial link text;Categories',
                 "endpoints":
                 { 
                  "news":'id;HeaderLink-news',
                  "entertainment": 'id;HeaderLink-entertainment'
                 },
                  "sub-endpoints":
                  {
                      "categories":{"news":'relies_prev:partial link text;News',
                                    "entertainment":'relies_prev:partial link text;Entertainment',
                                    "lad_originals":'relies_prev:partial link text;LAD Originals'
                                    },
                      "lad_originals":{"article":"rand_ind:css selector;contentWrapper"}
                  }
                 }
                }]