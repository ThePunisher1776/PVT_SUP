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
                {"https://www.ladbible.com":
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
                  "random": 'id;nav_random_li',
                  "article": 'rand_ind:class name;hp_thumb' 
                 },
                  "sub-endpoints":
                  {
                      "explore":{"coupons":'relies_prev:partial link text;Coupons',
                                    "tech_help_pro":'relies_prev:partial link text;Tech Help Pro',
                                    "random_article":'relies_prev:partial link text;Random Article',
                                    "about_us":'relies_prev:partial link text;About Us',
                                    "quizzes":'relies_prev:partial link text;Quizzes',
                                    "contribute":'relies_prev:partial link text;Contribute',
                                    "train_your_brain":'relies_prev:partial link text;Train Your Brain Game',
                                    "improve_your_english":'relies_prev:partial link text;Improve Your English',
                                    "popular_categories":'relies_prev:partial link text;Popular Categories',
                                    "arts_and_entertainment":'relies_prev:partial link text;Arts and Entertainment',
                                    },
                      "help_us":{"support_wikiHow":'relies_prev:partial link text;Support wikiHow',
                                 "community_dashboard":'relies_prev:partial link text;Community Dashboard',
                                 "write_an_article":'relies_prev:partial link text;Write an Article',
                                 "request_a_new_article":'relies_prev:partial link text;Request a New Article',
                                 "more_ideas":'relies_prev:partial link text;More Ideas...'
                                 },
                      "login_page":{"facebook":'relies_prev:partial link text;Facebook',
                                    "google":'relies_prev:partial link text;Google'
                                    }
                  }
                 }
                },
                {"https://www.yelp.com":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                  "login-page":   'partial link text;Log In',
                  "sign-up": 'partial link text;Sign Up',
                  "restaurants": 'partial link text;Restaurants',
                  "home-services": 'partial link text;Home Services',
                  "auto-services": 'partial link text; Auto Services',
                  "more": 'partial link text;More',
                  "yelp-for-business":'partial link text;Yelp for Business',
                  "article":  'rand_ind:class name;css-vzslx5'
                 },
                  "sub-endpoints":
                  {
                      "restaurants":{"delivery":'relies_prev:partial link text;Delivery',
                                     "burgers":'relies_prev:partial link text;Burgers',
                                     "chinese":'relies_prev:partial link text;Chinese',
                                     "italian":'relies_prev:partial link text;Italian',
                                     "reservations":'relies_prev:partial link text;Reservations',
                                     "japanese":'relies_prev:partial link text;Japanese',
                                     "thai":'relies_prev:partial link text;Thai',
                                     "mexican":'relies_prev:partial link text;Mexican'
                                     },
                      "home-services":{"contractors":'relies_prev:partial link text;Contractors',
                                       "electricians":'relies_prev:partial link text;Electricians',
                                       "home-cleaners":'relies_prev:partial link text;Home Cleaners',
                                       "hvac":'relies_prev:partial link text;HVAC',
                                       "landscaping":'relies_prev:partial link text;Landscaping',
                                       },
                      "auto-services":{"auto-repair":'relies_prev:partial link text;Auto Repair',
                                       "auto-detailing":'relies_prev:partial link text;Auto Detailing',
                                       "body-shops":'relies_prev:partial link text;Body Shops',
                                       "car-wash":'relies_prev:partial link text;Car Wash',
                                       "car-dealers":'relies_prev:partial link text;Car Dealers'
                                       },
                      "more":{"dry-cleaning":'relies_prev:partial link text;',
                              "phone-repair":'relies_prev:partial link text;',
                              "bars":'relies_prev:partial link text;',
                              "nightlife":'relies_prev:partial link text;',
                              "hair-salons":'relies_prev:partial link text;'
                              },
                      "yelp-for-business":{"add-a-business":'relies_prev:partial link text;Add a Business',
                                           "claim-your-business":'relies_prev:partial link text;Claim your business',
                                           "log-in-to-business-account":'relies_prev:partial link text;Log in to Business Account',
                                           "explore-yelp-for-business":'relies_prev:partial link text;Explore Yelp for Business'
                                           }
                  }
                 }
                },
                {"https://www.w3schools.com":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                  "tutorials":'id;navbtn_tutorials',
                  "references":'id;navbtn_references',
                  "exercises":'id;navbtn_exercises',
                  "login":'id;w3loginbtn',
                  "sign-up":'id;signupbtn_topnav',
                  "get-certified":'id;cert_navbtn',
                  "bootcamps":'partial link text;Bootcamp',
                  "learn-randomizer":'rand_ind:partial link text;Learn'
                 },
                  "sub-endpoints":
                  {
                      "tutorials":{"learn-html":'relies_prev:partial link text;Learn HTML',
                                   "learn-javascript":'relies_prev:partial link text;Learn JavaScript',
                                   "learn-sql:":'relies_prev:partial link text;Learn SQL',
                                   "learn-ai":'relies_prev:partial link text;Learn AI',
                                   "learn-python":'relies_prev:partial link text;Learn Python'
                                   },
                       "references":{"html-tag-reference":'relies_prev:partial link text;HTML Tag Reference',
                                     "javascript-reference":'relies_prev:partial link text;JavaScript Reference',
                                     "sql-reference":'relies_prev:partial link text;SQL Reference',
                                     "python-reference":'relies_prev:partial link text;Python Reference',
                                     "css-selector-reference":'relies_prev:partial link text;CSS Selector Reference',
                                     },
                       "exercises":{"html-exercises":'relies_prev:partial link text;HTML Exercises',
                                    "pandas-exercises":'relies_prev:partial link text;Pandas Exercises',
                                    "kotlin-exercises":'relies_prev:partial link text;Kotlin Exercises',
                                    "typescript-exercises":'relies_prev:partial link text;TypeScript Exercises',
                                    "excel-exercises":'relies_prev:partial link text;Excel Exercises'
                                    }
                  }
                 }
                },
                {"https://www.washingtonpost.com/":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                  "login-page":   'partial link text;Sign in',
                  "subscribe":  'partial link text;Subscribe',
                  "politics":'partial link text;Politics',
                  "opinions":'partial link text;Opinions',
                  "investigations":'partial link text;Investigations',
                  "climate":'partial link text;Climate'
                 },
                  "sub-endpoints":
                  {
                      "investigations":{"article":'rand_ind~relies_prev:css selector;.gray-darkest'},
                      "politics":{"article":'rand_ind~relies_prev:css selector;.gray-darkest'},
                      "opinions":{"article":'rand_ind~relies_prev:css selector;.gray-darkest'},                      "investigations":{"article":'relies-prev~relies_prev:css selector;.gray-darkest'},                      "investigations":{"article":'relies-prev~relies_prev:css selector;.gray-darkest'},                      
                      "climate":{"article":'rand_ind~relies_prev:css selector;.gray-darkest'}
                  }
                 }
                },
                {"https://www.godaddy.com/":
                {"specifics":"ablock=true;",
                 "main-menu":'refresh_sens:css selector;.pqzxpf0',
                 "endpoints":
                 { 
                  "login-page":   'css selector;.auov0ko',
                  "priced-service-rand":'rand_ind:css selector;.g142dare',
                  "domain-names":'relies_prev:css selector;#id-b523f8c3-cc8f-436b-a8af-3f0821e411b3 > div.f1aylcmx > div.ptfv6gx > ul > li:nth-child(1) > button',
                  "websites-and-hosting":'relies_prev:css selector;#id-b523f8c3-cc8f-436b-a8af-3f0821e411b3 > div.f1aylcmx > div.ptfv6gx > ul > li:nth-child(2) > button',
                  "email-and-marketing":'relies_prev:css selector;#id-b523f8c3-cc8f-436b-a8af-3f0821e411b3 > div.f1aylcmx > div.ptfv6gx > ul > li:nth-child(3) > button',
                  "hire-an-expert":'relies_prev:css selector;#id-b523f8c3-cc8f-436b-a8af-3f0821e411b3 > div.f1aylcmx > div.ptfv6gx > ul > li:nth-child(4) > button'     
                 },
                  "sub-endpoints":
                  {
                      "domain-names":{"search-for-domain-names":'relies_prev:partial link text;Search for Domain Names',
                                      "domain-broker-service":'relies_prev:partial link text;Domain Broker Services',
                                      "auctions-for-domain-names":'relies_prev:partial link text;Auctions for Domain Names',
                                      "domain-value-appraisal":'relies_prev:partial link text;Domain Value Appraisal',
                                      "save-with-bundles":'relies_prev:partial link text;Save with Bundles',
                                      },
                      "websites-and-hosting":{"website-builder":'relies_prev:partial link text;Website Builder',
                                              "web-hosting":'relies_prev:partial link text;Web Hosting',
                                              "website-security":'relies_prev:partial link text;Website Security',
                                              "online-store":'relies_prev:partial link text;Online Store',
                                              "back-up-your-website":'relies_prev:partial link text;Back Up Your Website',
                                              },

                      "email-and-marketing":{"email-and-microsoft":'relies_prev:partial link text;Email & Microsoft 365',
                                             "digital-marketing-suite":'relies_prev:partial link text;Digital Marketing Suite',
                                             "content-and-photo-creator":'relies_prev:partial link text;Content & Photo Creator'
                                             },
                      "hire-an-expert":{"website-design-services":'relies_prev:partial link text;Website Design Services',
                                        "digital-marketing-services":'relies_prev:partial link text;Digital Marketing Services'
                                        }
                  }
                 }
                },
                {"https://www.etsy.com/":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                  "login-page":   'css selector;#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button',
                  "popular-gifts":'rand_ind:css selector;.popular-right-now',
                  "shop-our-selections-and-fresh-from-blog":'rand_ind:css selector;.wt-card a.wt-card__link',
                  "top-nav-random":'rand_ind:css selector;.cat-nav .top-nav-item'
                 },
                  "sub-endpoints":
                  {
                      "top-nav-articles":{"articles":'relies_prev~rand_ind:css selector;.v2-listing-card__img'}
                  }
                 }
                },
                {"https://www.softonic.com/":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                  "game":'rand_ind:css selector;.card-app__img',
                  "apps":'ind_0:class name;menu-featured__item',
                  "games":'ind_1:class name;menu-featured__item',
                  "news":'ind_2:class name;menu-featured__item'
                 },
                  "sub-endpoints":
                  {
                      "apps":{"app":'relies_prev~rand_ind:class name;app-info__name'},
                      "games":{"game":'relies_prev~randd:css selector;.card-game__cover'},
                      "news":{"article":'rand_ind:css selector;.card-article__link'}
                  }
                 }
                },
                {"https://www.9gag.com/":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                  "game":'rand_ind:css selector;.card-app__img',
                  "interests":''
                 },
                  "sub-endpoints":
                  {
                      "apps":{"app":'relies_prev~rand_ind:class name;app-info__name'},
                      "games":{"game":'relies_prev~randd:css selector;.card-game__cover'},
                      "news":{"article":'rand_ind:css selector;.card-article__link'}
                  }
                 }
                }
                ]
