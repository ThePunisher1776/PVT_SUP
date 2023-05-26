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
                {"https://www.playstation.com":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                     "hardware-games":'rand_ind:css selector;.gdk .featured-hardware .slider__controls .slider__control figcaption',
                     "hardware":'refresh_sens:id;menu-button-primary--msg-hardware',
                     "games":'refresh_sens:id;menu-button-primary--msg-hardware',
                     "services":'refresh_sens:id;menu-button-primary--msg-hardware',
                     "news":'refresh_sens:id;menu-button-primary--msg-hardware',
                     "shop":'refresh_sens:id;menu-button-primary--msg-hardware',
                     "support":'refresh_sens:id;menu-button-primary--msg-support'
                 },
                  "sub-endpoints":
                  {
                      "games":{"ps5":'link-secondary--msg-ps5',
                               "ps4":'link-secondary--msg-ps5',
                               "ps-vr2":'link-secondary--msg-ps5',
                               "ps-plus":'link-secondary--msg-ps5',
                               "buy-games":'link-secondary--msg-ps5',
                               }
                  }
                 }
                },
                {"https://www.square-enix-games.com/en_US/home":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                     "store":'partial link text;STORE',
                     "more":'partial link text;MORE',
                     "support":'partial link text;SUPPORT',
                     "games":'id;topgames-button'
                 },
                  "sub-endpoints":
                  {
                      "store":{"games":'rand_ind~relies_prev:class name;card-img-container'},
                      "support":{"articles":'rand_ind~relies_prev:css selector;.b',
                                 "articles2":'rand_ind~relies_prev:css selector;fieldset, img, abbr'},
                      "games":{"games":'relies_prev:partial link text;VIEW MORE'}
                  }
                 }
                },
                {"vmware.com":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                     "multi-cloud-services":'ind_0:css selector;.menu-item li',
                     "products":'ind_1:css selector;.menu-item li',
                     "solutions":'ind_2:css selector;.menu-item li',
                     "partners":'ind_3:css selector;.menu-item li',
                     "resources":'ind_4:css selector;.menu-item li'
                 },
                  "sub-endpoints":
                  {
                      "resources":{"relies_prev:partial link text;Blogs",
                                   "relies_prev:partial link text;Podcasts",
                                   "relies_prev:partial link text;Communities",
                                   "relies_prev:partial link text;Customer Stories",
                                   "relies_prev:partial link text;SprineOne",
                                   "relies_prev:partial link text;Cloud Marketplace"},
                      "partners":{"relies_prev:partial link text;Become a Cloud Provider",
                                  "relies_prev:partial link text;Cloud Partner Navigator",
                                  "relies_prev:partial link text;Get Cloud Verified",
                                  "relies_prev:partial link text;Partner Connect Login",
                                  "relies_prev:partial link text;Work with VMware"},
                      "solutions":{"relies_prev:partial link text;Communications Service Providers",
                                   "relies_prev:partial link text;Federal Government",
                                   "relies_prev:partial link text;Financial Services",
                                   "relies_prev:partial link text;Healthcare Providers"}
                  }
                 }
                },
                {"nationalgeographic.com":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                     "article":'rand_ind:css selector;.ListItem__Link',
                     "login": 'ind_0:class name;NavBar__List--item',
                     "newsletters":'ind_2:class name;NavBar__List--item',
                     "subscribe": 'ind_3:class name;NavBar__List--item',
                     "menu":'ind_4:class name;NavBar__List--item',
                     "latest-stories":'rand_ind:css selector;.HomepagePromos__row'
                 },
                  "sub-endpoints":
                  {
                      "newsletters":{"article":'relies_prev~rand_ind:class name;CheckCard__Link'},
                      "menu":{"topics":'relies_prev~rand_ind:css selector;.MenuModal__Content__List__Item--primarylink, .MenuModal__Content__List__Item--primarylink:focus, .MenuModal__Content__List__Item--primarylink:hover, .MenuModal__Content__List__Item--secondarylink:focus, .MenuModal__Content__List__Item--secondarylink:hover',
                              "sites":'relies_prev~rand_ind:css selector.MenuModal__Content__List__Item--secondarylink'}
                  }
                 }
                },
                {"foodnetwork.ca":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                     "recipes":'ind_0:class name;nav-link',
                     "chefs-hosts":'ind_1:class name;nav-link',
                     "shows":'ind_2:class name;nav-link',
                     "where-to-watch":'ind_3:class name;nav-link',
                     "articles":'rand_ind:css selector;.post-block__title a'
                 },
                  "sub-endpoints":
                  {
                     "recipes":{"recipe":'relies_prev~rand_ind:class name;post-block__title'},
                     "chefs-hosts":{"host":'ind_1:css selector;.chefs-hosts__grid__item, .shows__grid__item'},
                     "shows":{"show":'relies_prev~rand_ind:class name;shows__grid__item'},
                     "where-to-watch":{"channels":'relies_prev~rand_ind:css selector;.where-to-watch .where-to-watch__channel_single .channel-logo img'}
                  }
                 }
                },
                {"informer.com":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                     "blog":'partial link text;Blog',
                     "about":'partial link text;About',
                     "contacts":'partial link text;Contacts',
                     "dmca":'partial link text;DMCA',
                     "projects":'rand_ind:css selector;.items_wrapper .item'
                 },
                  "sub-endpoints":
                  {
                      "blog":{"articles":"relies_prev~rand_ind:css selector;.news a",
                              "types":'relies_prev~rand_ind:css selector;.items_wrapper .item'}
                  }
                 }
                },
                {"malwarebytes.com":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                     "personal":'ind_0:css selector;#mbnav.mainnav .navitem .navitem-btn',
                     "business":'ind_1:css selector;#mbnav.mainnav .navitem .navitem-btn',
                     "pricing":'ind_2:css selector;#mbnav.mainnav .navitem .navitem-btn',
                     "partners":'ind_3:css selector;#mbnav.mainnav .navitem .navitem-btn',
                     "resources":'ind_4:css selector;#mbnav.mainnav .navitem .navitem-btn',
                     "support":'ind_5:css selector;#mbnav.mainnav .navitem .navitem-btn',
                 },
                  "sub-endpoints":
                  {
                      "personal":{"android":'relies_prev:direct-link;android',
                                  "mac":'relies_prev:direct-link;mac',
                                  "chromebook":'relies_prev:direct-link;chromebook',
                                  "ios":'relies_prev:direct-link;ios',
                                  "teams":'relies_prev:direct-link;teams'},
                      "business":{"eps":'relies_prev:partial link text;Endpoint Protection for Servers',
                                  "edrs":'relies_prev:partial link text;Endpoint Detection & Response for Servers',
                                  "ir":'relies_prev:partial link text;Incident Response',
                                  "npa":'relies_prev:partial link text;Nebula Platform Architecture'},
                      "pricing":{"business":'relies_prev:direct-link;business/pricing',
                                 "small-office":'relies_prev:direct-link;pricing/teams',
                                 "personal":'relies_prev:direct-link;pricing'},
                      "partners":{"resellers":'relies_prev:partial link text;Resellers',
                                  "managed-service-providers":'relies_prev:partial link text;Managed Service Providers',
                                  "pc-repair":'relies_prev:partial link text;Computer Repair',
                                  "tech-repairs":'relies_prev:partial link text;Technology Repairs'}
                  }
                 }
                }
]
