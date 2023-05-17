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
                          
                      }
                  }
                 }
                }, 
                {"https://ladbible.com":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:class name;css-20as6p',
                 "endpoints":
                 { 
                  "news":'id;HeaderLink-news',
                  "entertainment": 'id;HeaderLink-entertainment',
                  "article": 'rand_ind:class name;contentWrapper'
                 },
                  "sub-endpoints":
                  {
                      "categories":{"news":'relies_prev:direct-link;news',
                                    "entertainment":'relies_prev:direct-link;entertainment',
                                    "lad_originals":'relies_prev:direct-link;originals'
                                    },
                      "news":{"article":"rand_ind:class name;contentWrapper"},
                      "entertainment":{"show":"rand_ind:class name;contentWrapper"},
                      "lad_originals":{"article":"rand_ind:class name;contentWrapper"}
                  }
                 }
                },

                {"https://www.wikihow.com/":
                {"specifics":"ablock=true;",
                 "endpoints":
                 {
                  "login-page":   'id;nav_profile',
                  "help-us":  'id;nav_help',
                  "explore": 'id;nav_explore',
                  "article": 'something' 
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
                      "login-page":{"facebook":'relies_prev:id;fb_login_head'
                          
                                  },
                      "trending":{"video":'rand_ind:css selector;ytd-video-renderer'
                                  },
                     
                  }
                 }
                },]