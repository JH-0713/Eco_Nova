import asyncio
import flet as fl
from certifi import contents
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    ElevatedButton, FilledButton, FilledTonalButton, View, Image, Size, Icon, control, Alignment, Row, \
    RoundedRectangleBorder, Margin, Padding, NavigationBar, NavigationBarDestination
from flet.controls.material.icons import Icons
import webbrowser


def main(page: fl.Page):
    # configurações
    page.title = "EcoNova"
    page.theme_mode = ThemeMode.LIGHT  # ThemeMode.LIGHT ou DARK
    page.window.width = 400
    page.window.height = 850

    # Funções
    def abrir_web(url):
        webbrowser.open(url)

    def ver_plastico():
        navigation("/plastico")

    def ver_papel():
        navigation("/papel")

    def ver_metal():
        navigation("/metal")

    def ver_vidro():
        navigation("/vidro")

    # Navegar
    def navigation(route):
        asyncio.create_task(
            page.push_route(route)
        )

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                scroll=fl.ScrollMode.ALWAYS,
                spacing=14,
                controls=[
                    # Barra inicial
                    fl.AppBar(
                        leading=Icon(icon=Icons.RECYCLING, color=Colors.GREEN_500, size=42),
                        leading_width=50,
                        title=Text("EcoNova", color="#29664C", size=22, weight=FontWeight.BOLD),
                        title_spacing=10,
                        toolbar_height=45,
                    ),

                    # Botoes e Texto
                    Container(
                        Column(
                            controls=[
                                Text("Qual é o Material que Deseja Reciclar Hoje?",
                                     size=25,
                                     text_align=fl.TextAlign.CENTER
                                     ),
                                Row(
                                    alignment=fl.MainAxisAlignment.CENTER,
                                    controls=[
                                        Column(
                                            controls=[
                                                Row(
                                                    controls=[
                                                        FilledButton("Plástico",
                                                                     on_click=lambda: ver_plastico(),
                                                                     icon=Icons.WATER_DROP_OUTLINED,
                                                                     icon_color="#065F46",
                                                                     width=120,
                                                                     height=100,
                                                                     bgcolor=Colors.GREY_200,
                                                                     color=Colors.GREY_800,
                                                                     style=fl.ButtonStyle(
                                                                         shape=RoundedRectangleBorder(radius=20), )
                                                                     ),
                                                        FilledButton("Papel",
                                                                     on_click=lambda: ver_papel(),
                                                                     icon=Icons.DESCRIPTION_OUTLINED,
                                                                     icon_color="#065F46",
                                                                     width=120,
                                                                     height=100,
                                                                     bgcolor=Colors.GREY_200,
                                                                     color=Colors.GREY_800,
                                                                     style=fl.ButtonStyle(
                                                                         shape=RoundedRectangleBorder(radius=20), ),
                                                                     ),
                                                    ]
                                                ),
                                                Row(
                                                    controls=[
                                                        FilledButton("Metal",
                                                                     on_click=lambda: ver_metal(),
                                                                     icon=Icons.PRECISION_MANUFACTURING_OUTLINED,
                                                                     icon_color="#065F46",
                                                                     width=120,
                                                                     height=100,
                                                                     bgcolor=Colors.GREY_200,
                                                                     color=Colors.GREY_800,
                                                                     style=fl.ButtonStyle(
                                                                         shape=RoundedRectangleBorder(radius=20))
                                                                     ),

                                                        FilledButton("Vidro",
                                                                     on_click=lambda: ver_plastico,
                                                                     icon=Icons.LOCAL_BAR_OUTLINED,
                                                                     icon_color="#065F46",
                                                                     width=120,
                                                                     height=100,
                                                                     bgcolor=Colors.GREY_200,
                                                                     color=Colors.GREY_800,
                                                                     style=fl.ButtonStyle(
                                                                         shape=RoundedRectangleBorder(radius=20))
                                                                     ),

                                                    ]
                                                ),
                                                FilledButton("Outros",
                                                             on_click=lambda: ver_plastico,
                                                             icon=Icons.STORE_OUTLINED,
                                                             icon_color="#065F46",
                                                             width=250,
                                                             height=120,
                                                             bgcolor=Colors.GREY_200,
                                                             color=Colors.GREY_800,
                                                             style=fl.ButtonStyle(
                                                                 shape=RoundedRectangleBorder(radius=35))
                                                             ),

                                            ]

                                        ),

                                    ],

                                ),

                            ],
                            spacing=20,

                        ),
                    ),
                    Container(
                        Column(
                            controls=[
                                Row(
                                    alignment=fl.MainAxisAlignment.CENTER,
                                    controls=[

                                        FilledButton("Encontre Areas de reciclagem em sua cidade...",
                                                     on_click=lambda: abrir_web(
                                                         "https://www.rotadareciclagem.com.br/"),
                                                     icon=Icons.LOCATION_ON,
                                                     icon_color="#595C5B",
                                                     width=300,
                                                     height=75,
                                                     bgcolor="#E0E3E1",
                                                     color=Colors.GREY_800,
                                                     style=fl.ButtonStyle(shape=RoundedRectangleBorder(radius=50))

                                                     ),
                                    ],
                                ),
                            ],
                            alignment=fl.MainAxisAlignment.CENTER,
                            horizontal_alignment=fl.CrossAxisAlignment.CENTER,
                            scroll=fl.ScrollMode.ALWAYS,
                        ),
                        alignment=fl.Alignment.CENTER,
                        width=400,
                        height=200,
                        padding=15,

                    ),

                ],

            )
        )



        if page.route == "/plastico":
            page.views.append(
                View(
                    route="/plastico",
                    scroll=fl.ScrollMode.ALWAYS,
                    controls=[
                        fl.AppBar(
                            title=Text("EcoNova", color="#29664C", size=22, weight=FontWeight.BOLD),
                            title_spacing=10,
                            toolbar_height=45,
                            actions=[
                                Icon(Icons.DELETE,
                                     color=Colors.RED,
                                     margin=Margin.only(right=15),
                                     )
                            ],

                        ),
                        # ARTESANATO DE RECICLAGEM
                        Container(
                            Column(
                                controls=[
                                    fl.Stack(
                                        width=350,
                                        height=150,
                                        controls=[
                                            # Imagem de fundo
                                            fl.Container(
                                                width=350,
                                                height=150,
                                                border_radius=fl.BorderRadius.all(20),
                                                clip_behavior=fl.ClipBehavior.HARD_EDGE,
                                                content=fl.Image(
                                                    src="https://trevoreciclagem.com.br/wp-content/uploads/2025/03/Reciclar-plastico_-saiba-como-fazer-certo.webp",
                                                    width=350,
                                                    height=150,
                                                    fit="cover"
                                                )
                                            ),
                                            fl.Container(
                                                width=350,
                                                height=150,
                                                alignment=fl.Alignment.BOTTOM_LEFT,
                                                padding=fl.Padding(10, 10, 10, 10),
                                                content=fl.Text(
                                                    "Plástico",
                                                    size=25,
                                                    weight=fl.FontWeight.BOLD,
                                                    style=fl.TextStyle(
                                                        color="#FAB2B2",
                                                        shadow=fl.BoxShadow(
                                                            color="orange",
                                                            blur_radius=15,
                                                            offset=fl.Offset(3, 3),

                                                        )
                                                    )
                                                )
                                            ),
                                        ]
                                    ),
                                    Container(
                                        content=Column(
                                            controls=[
                                                Row(
                                                    controls=[
                                                        Text(f"Instruções de Descarte:",
                                                             size=18,
                                                             weight=FontWeight.BOLD,
                                                             color="#797D7C",
                                                             italic=True
                                                             ),
                                                    ],
                                                    margin=Margin.only(left=15),
                                                ),
                                                Container(
                                                    content=Column(
                                                        controls=[
                                                            Row(
                                                                controls=[
                                                                    Container(
                                                                        width=45,
                                                                        height=45,
                                                                        bgcolor="#FABABA",
                                                                        border_radius=25,
                                                                        alignment=Alignment.CENTER,
                                                                        content=Icon(Icons.CLEAN_HANDS, color="#B62D2B")
                                                                    ),
                                                                    Column(
                                                                        controls=[
                                                                            Text("Lavar e Secar",
                                                                                 size=15,
                                                                                 weight=FontWeight.BOLD
                                                                                 ),
                                                                            Text(
                                                                                "Remova resíduos de comida para evitar contaminação.",
                                                                                width=235
                                                                            )
                                                                        ],
                                                                        spacing=2,
                                                                        margin=Margin.only(top=15)

                                                                    )
                                                                ]
                                                            ),
                                                            Row(
                                                                controls=[
                                                                    Container(
                                                                        width=45,
                                                                        height=45,
                                                                        bgcolor="#FABABA",
                                                                        border_radius=25,
                                                                        alignment=Alignment.CENTER,
                                                                        content=Icon(
                                                                            Icons.VERTICAL_ALIGN_CENTER_OUTLINED,
                                                                            color="#B62D2B")
                                                                    ),
                                                                    Column(
                                                                        controls=[
                                                                            Text("Compactar Embalagens",
                                                                                 size=15,
                                                                                 weight=FontWeight.BOLD
                                                                                 ),
                                                                            Text(
                                                                                "Reduza o volume para otimizar o transporte.",
                                                                                width=265
                                                                            )
                                                                        ],
                                                                        spacing=2,
                                                                        margin=Margin.only(top=15)

                                                                    )
                                                                ],
                                                            ),
                                                            Row(
                                                                controls=[
                                                                    Container(
                                                                        width=45,
                                                                        height=45,
                                                                        bgcolor="#FABABA",
                                                                        border_radius=25,
                                                                        alignment=Alignment.CENTER,
                                                                        content=Icon(Icons.BACKSPACE, color="#B62D2B"),
                                                                        scale=fl.Scale(scale_x=-1, scale_y=1)
                                                                    ),
                                                                    Column(
                                                                        controls=[
                                                                            Text("Remover Rótulos",
                                                                                 size=15,
                                                                                 weight=FontWeight.BOLD
                                                                                 ),
                                                                            Text(
                                                                                "Separe adesivos e lacres de metal quando possível.",
                                                                                width=265
                                                                            )
                                                                        ],
                                                                        spacing=2,
                                                                        margin=Margin.only(top=15)

                                                                    )
                                                                ]
                                                            ),

                                                        ],
                                                        margin=Margin.only(left=30),
                                                        spacing=2
                                                    )
                                                ),
                                            ],
                                            spacing=1
                                        ),
                                    ),

                                    Container(
                                        content=Column(
                                            controls=[
                                                Row(
                                                    controls=[
                                                        Text(f"Encontre Ecopontos Proximos:",
                                                             size=18,
                                                             weight=FontWeight.BOLD,
                                                             color="#797D7C",
                                                             italic=True
                                                             ),
                                                    ],
                                                    margin=Margin.only(left=15),
                                                ),
                                                Container(
                                                    content=Column(
                                                        controls=[

                                                            FilledButton(
                                                                "Veja Áreas de Reciclagem em sua Cidade...",
                                                                Container(
                                                                    width=25,
                                                                    height=25,
                                                                    alignment=Alignment.CENTER,
                                                                    content=Icon(Icons.LOCATION_ON, color="#B62D2B"),
                                                                    scale=fl.Scale(scale_x=-1, scale_y=1)
                                                                ),
                                                                on_click=lambda: abrir_web(
                                                                    "https://www.rotadareciclagem.com.br/"),
                                                                icon_color="#595C5B",
                                                                width=300,
                                                                height=60,
                                                                bgcolor="#FABABA",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=15))

                                                            ),
                                                        ],
                                                        margin=Margin.only(left=30),
                                                        spacing=8
                                                    )
                                                ),
                                            ],
                                            spacing=10
                                        ),
                                    ),
                                    Container(
                                        content=Column(
                                            controls=[
                                                Row(
                                                    controls=[
                                                        Text(f"Sites:",
                                                             size=18,
                                                             weight=FontWeight.BOLD,
                                                             color="#797D7C",
                                                             italic=True
                                                             ),
                                                    ],
                                                    margin=Margin.only(left=15),
                                                ),
                                                Container(
                                                    content=Row(
                                                        controls=[

                                                            FilledButton(
                                                                Text("Ver mais sobre",
                                                                     size=11, weight=FontWeight.BOLD),

                                                                on_click=lambda: abrir_web(
                                                                    "https://exame.com/esg/reciclagem-de-plastico-como-e-o-processo/"),
                                                                icon_color="#595C5B",
                                                                width=100,
                                                                height=60,
                                                                bgcolor="#FABABA",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=20))

                                                            ),
                                                            FilledButton(
                                                                Text("Ideias reciclagem",
                                                                     size=11, weight=FontWeight.BOLD),

                                                                on_click=lambda: abrir_web(
                                                                    "https://www.totalconstrucao.com.br/ideias-de-reciclagem/"),
                                                                icon_color="#595C5B",
                                                                width=105,
                                                                height=60,
                                                                bgcolor="#FABABA",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=20))

                                                            ),

                                                            FilledButton(
                                                                Text("Canal Youtube",
                                                                     size=11, weight=FontWeight.BOLD),

                                                                on_click=lambda: abrir_web(
                                                                    "https://www.bing.com/ck/a?!&&p=45a05aee6fc45c1b556ac50d9e7364326d2ced6581bd32b0b039d49cfd1ecb6eJmltdHM9MTc3NTUyMDAwMA&ptn=3&ver=2&hsh=4&fclid=184f7c95-ae16-69e5-048e-6a78af3b687c&psq=e%0aIder+Alves+-+DIY+Moda+Fashio&u=a1aHR0cHM6Ly93d3cueW91dHViZS5jb20vY2hhbm5lbC9VQzl1V0ZfdGdYdTQ0Zlh4bUs1azhGMUE"),
                                                                icon_color="#595C5B",
                                                                width=100,
                                                                height=60,
                                                                bgcolor="#FABABA",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=20))

                                                            ),
                                                        ],

                                                        margin=Margin.only(left=30),
                                                        spacing=8
                                                    ),

                                                ),
                                            ],
                                            spacing=10
                                        ),
                                    )
                                ],
                                spacing=15,
                                scroll=fl.ScrollMode.ALWAYS,
                            ),

                        ),

                    ],
                    spacing=15,
                ),

            )

        if page.route == "/papel":
            page.views.append(
                View(
                    route="/papel",
                    scroll=fl.ScrollMode.ALWAYS,
                    controls=[
                        fl.AppBar(
                            title=Text("EcoNova", color="#29664C", size=22, weight=FontWeight.BOLD),
                            title_spacing=10,
                            toolbar_height=45,
                            actions=[
                                Icon(Icons.DELETE,
                                     color=Colors.BLUE,
                                     margin=Margin.only(right=15),
                                     )
                            ],
                        ),
                        # ARTESANATO DE RECICLAGEM
                        Container(
                            Column(
                                controls=[
                                    fl.Stack(
                                        width=350,
                                        height=150,
                                        controls=[
                                            # Imagem de fundo
                                            fl.Container(
                                                width=350,
                                                height=150,
                                                border_radius=fl.BorderRadius.all(20),
                                                clip_behavior=fl.ClipBehavior.HARD_EDGE,
                                                content=fl.Image(
                                                    src="https://t4.ftcdn.net/jpg/07/65/84/53/360_F_765845311_KOiX3LEEgw1F9ozmAFGlgwQVamSKPaAU.jpg",
                                                    width=350,
                                                    height=150,
                                                    fit="cover"
                                                )
                                            ),
                                            fl.Container(
                                                width=350,
                                                height=150,
                                                alignment=fl.Alignment.BOTTOM_LEFT,
                                                padding=fl.Padding(10, 10, 10, 10),
                                                content=fl.Text(
                                                    "Papel",
                                                    size=25,
                                                    weight=fl.FontWeight.BOLD,
                                                    style=fl.TextStyle(
                                                        color="#95FFFA",
                                                        shadow=fl.BoxShadow(
                                                            color="purple",
                                                            blur_radius=15,
                                                            offset=fl.Offset(3, 3),

                                                        )
                                                    )
                                                )
                                            ),
                                        ]
                                    ),
                                    Container(
                                        content=Column(
                                            controls=[
                                                Row(
                                                    controls=[
                                                        Text(f"Instruções de Descarte:",
                                                             size=18,
                                                             weight=FontWeight.BOLD,
                                                             color="#797D7C",
                                                             italic=True
                                                             ),
                                                    ],
                                                    margin=Margin.only(left=15),
                                                ),
                                                Container(
                                                    content=Column(
                                                        controls=[
                                                            Row(
                                                                controls=[
                                                                    Container(
                                                                        width=45,
                                                                        height=45,
                                                                        bgcolor="#95FFFA",
                                                                        border_radius=25,
                                                                        alignment=Alignment.CENTER,
                                                                        content=Icon(Icons.RECYCLING_ROUNDED,
                                                                                     color="#00A5FF")
                                                                    ),
                                                                    Column(
                                                                        controls=[
                                                                            Text("Separação de Materiais",
                                                                                 size=15,
                                                                                 weight=FontWeight.BOLD
                                                                                 ),
                                                                            Text(
                                                                                "Remova resíduos de comida ou produtos químicos do papel.",
                                                                                width=255
                                                                            )
                                                                        ],
                                                                        spacing=2,
                                                                        margin=Margin.only(top=15)

                                                                    )
                                                                ]
                                                            ),
                                                            Row(
                                                                controls=[
                                                                    Container(
                                                                        width=45,
                                                                        height=45,
                                                                        bgcolor="#95FFFA",
                                                                        border_radius=25,
                                                                        alignment=Alignment.CENTER,
                                                                        content=Icon(
                                                                            Icons.VERTICAL_ALIGN_CENTER_OUTLINED,
                                                                            color="#00A5FF")
                                                                    ),
                                                                    Column(
                                                                        controls=[
                                                                            Text("Compactar Embalagen",
                                                                                 size=15,
                                                                                 weight=FontWeight.BOLD
                                                                                 ),
                                                                            Text(
                                                                                "Use caixas de papelão achatadas e remova fitas adesivas.",
                                                                                width=265
                                                                            )
                                                                        ],
                                                                        spacing=2,
                                                                        margin=Margin.only(top=15)

                                                                    )
                                                                ],
                                                            ),
                                                            Row(
                                                                controls=[
                                                                    Container(
                                                                        width=45,
                                                                        height=45,
                                                                        bgcolor="#95FFFA",
                                                                        border_radius=25,
                                                                        alignment=Alignment.CENTER,
                                                                        content=Icon(Icons.ASSIGNMENT, color="#00A5FF"),
                                                                        scale=fl.Scale(scale_x=-1, scale_y=1)
                                                                    ),
                                                                    Column(
                                                                        controls=[
                                                                            Text("Seguir a coleta seletiva",
                                                                                 size=15,
                                                                                 weight=FontWeight.BOLD
                                                                                 ),
                                                                            Text(
                                                                                "Verifique os pontos de coleta seletiva do município.",
                                                                                width=265
                                                                            )
                                                                        ],
                                                                        spacing=2,
                                                                        margin=Margin.only(top=15)

                                                                    )
                                                                ]
                                                            ),

                                                        ],
                                                        margin=Margin.only(left=30),
                                                        spacing=2
                                                    )
                                                ),
                                            ],
                                            spacing=1
                                        ),
                                    ),

                                    Container(
                                        content=Column(
                                            controls=[
                                                Row(
                                                    controls=[
                                                        Text(f"Encontre Ecopontos Proximos:",
                                                             size=18,
                                                             weight=FontWeight.BOLD,
                                                             color="#797D7C",
                                                             italic=True
                                                             ),
                                                    ],
                                                    margin=Margin.only(left=15),
                                                ),
                                                Container(
                                                    content=Column(
                                                        controls=[

                                                            FilledButton(
                                                                "Veja Áreas de Reciclagem em sua Cidade...",
                                                                Container(
                                                                    width=25,
                                                                    height=25,
                                                                    alignment=Alignment.CENTER,
                                                                    content=Icon(Icons.LOCATION_ON, color="#00A5FF"),
                                                                    scale=fl.Scale(scale_x=-1, scale_y=1)
                                                                ),
                                                                on_click=lambda: abrir_web(
                                                                    "https://www.rotadareciclagem.com.br/"),
                                                                icon_color="#595C5B",
                                                                width=300,
                                                                height=60,
                                                                bgcolor="#95FFFA",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=15))

                                                            ),
                                                        ],
                                                        margin=Margin.only(left=30),
                                                        spacing=8
                                                    )
                                                ),
                                            ],
                                            spacing=10
                                        ),
                                    ),
                                    Container(
                                        content=Column(
                                            controls=[
                                                Row(
                                                    controls=[
                                                        Text(f"Sites:",
                                                             size=18,
                                                             weight=FontWeight.BOLD,
                                                             color="#797D7C",
                                                             italic=True
                                                             ),
                                                    ],
                                                    margin=Margin.only(left=15),
                                                ),
                                                Container(
                                                    content=Row(
                                                        controls=[

                                                            FilledButton(
                                                                Text("Ver mais sobre",
                                                                     size=11, weight=FontWeight.BOLD),

                                                                on_click=lambda: abrir_web(
                                                                    "https://ambiental.sc/blog/como-e-feita-a-reciclagem-de-papel/"),
                                                                icon_color="#595C5B",
                                                                width=100,
                                                                height=60,
                                                                bgcolor="#95FFFA",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=20))

                                                            ),
                                                            FilledButton(
                                                                Text("Ideias reciclagem",
                                                                     size=11, weight=FontWeight.BOLD),

                                                                on_click=lambda: abrir_web(
                                                                    "https://br.pinterest.com/viladoartesao/artesanato-com-papel/"),
                                                                icon_color="#595C5B",
                                                                width=105,
                                                                height=60,
                                                                bgcolor="#95FFFA",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=20))

                                                            ),

                                                            FilledButton(
                                                                Text("Canal Youtube",
                                                                     size=11, weight=FontWeight.BOLD),

                                                                on_click=lambda: abrir_web(
                                                                    "https://www.youtube.com/playlist?list=PLg54jVJRnbpi8G5DbizNnlptahTlEKXwy"),
                                                                icon_color="#595C5B",
                                                                width=100,
                                                                height=60,
                                                                bgcolor="#95FFFA",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=20))

                                                            ),
                                                        ],

                                                        margin=Margin.only(left=30),
                                                        spacing=8
                                                    ),

                                                ),
                                            ],
                                            spacing=10
                                        ),
                                    )
                                ],
                                spacing=15,
                                scroll=fl.ScrollMode.ALWAYS,
                            ),

                        ),

                    ],
                    spacing=5,
                ),

            )

        if page.route == "/metal":
            page.views.append(
                View(
                    route="/metal",
                    scroll=fl.ScrollMode.ALWAYS,
                    controls=[
                        fl.AppBar(
                            title=Text("EcoNova", color="#29664C", size=22, weight=FontWeight.BOLD),
                            title_spacing=10,
                            toolbar_height=45,
                            actions=[
                                Icon(Icons.DELETE,
                                     color=Colors.YELLOW,
                                     margin=Margin.only(right=15),
                                     )
                            ],
                        ),
                        # ARTESANATO DE RECICLAGEM
                        Container(
                            Column(
                                controls=[
                                    fl.Stack(
                                        width=350,
                                        height=150,
                                        controls=[
                                            # Imagem de fundo
                                            fl.Container(
                                                width=350,
                                                height=150,
                                                border_radius=fl.BorderRadius.all(20),
                                                clip_behavior=fl.ClipBehavior.HARD_EDGE,
                                                content=fl.Image(
                                                    src="https://img.freepik.com/fotos-premium/um-recipiente-amarelo-sobre-um-fundo-amarelo_803126-5991.jpg?semt=ais_hybrid&w=740&q=80",
                                                    width=350,
                                                    height=150,
                                                    fit="cover"
                                                )
                                            ),
                                            fl.Container(
                                                width=350,
                                                height=150,
                                                alignment=fl.Alignment.BOTTOM_LEFT,
                                                padding=fl.Padding(10, 10, 10, 10),
                                                content=fl.Text(
                                                    "Metal",
                                                    size=25,
                                                    weight=fl.FontWeight.BOLD,
                                                    style=fl.TextStyle(
                                                        color="#FFD980",
                                                        shadow=fl.BoxShadow(
                                                            color="red",
                                                            blur_radius=15,
                                                            offset=fl.Offset(3, 3),

                                                        )
                                                    )
                                                )
                                            ),
                                        ]
                                    ),
                                    Container(
                                        content=Column(
                                            controls=[
                                                Row(
                                                    controls=[
                                                        Text(f"MUDAR OS TOPICOS!!!!:",
                                                             size=18,
                                                             weight=FontWeight.BOLD,
                                                             color="#797D7C",
                                                             italic=True
                                                             ),
                                                    ],
                                                    margin=Margin.only(left=15),
                                                ),
                                                Container(
                                                    content=Column(
                                                        controls=[
                                                            Row(
                                                                controls=[
                                                                    Container(
                                                                        width=45,
                                                                        height=45,
                                                                        bgcolor="#FFD980",
                                                                        border_radius=25,
                                                                        alignment=Alignment.CENTER,
                                                                        content=Icon(Icons.RECYCLING_ROUNDED,
                                                                                     color="#FFAA01")
                                                                    ),
                                                                    Column(
                                                                        controls=[
                                                                            Text("Separação de Materiais",
                                                                                 size=15,
                                                                                 weight=FontWeight.BOLD
                                                                                 ),
                                                                            Text(
                                                                                "Remova resíduos de comida ou produtos químicos do papel.",
                                                                                width=255
                                                                            )
                                                                        ],
                                                                        spacing=2,
                                                                        margin=Margin.only(top=15)

                                                                    )
                                                                ]
                                                            ),
                                                            Row(
                                                                controls=[
                                                                    Container(
                                                                        width=45,
                                                                        height=45,
                                                                        bgcolor="#FFD980",
                                                                        border_radius=25,
                                                                        alignment=Alignment.CENTER,
                                                                        content=Icon(
                                                                            Icons.VERTICAL_ALIGN_CENTER_OUTLINED,
                                                                            color="#FFAA01")
                                                                    ),
                                                                    Column(
                                                                        controls=[
                                                                            Text("Compactar Embalagen",
                                                                                 size=15,
                                                                                 weight=FontWeight.BOLD
                                                                                 ),
                                                                            Text(
                                                                                "Use caixas de papelão achatadas e remova fitas adesivas.",
                                                                                width=265
                                                                            )
                                                                        ],
                                                                        spacing=2,
                                                                        margin=Margin.only(top=15)

                                                                    )
                                                                ],
                                                            ),
                                                            Row(
                                                                controls=[
                                                                    Container(
                                                                        width=45,
                                                                        height=45,
                                                                        bgcolor="#FFD980",
                                                                        border_radius=25,
                                                                        alignment=Alignment.CENTER,
                                                                        content=Icon(Icons.ASSIGNMENT, color="#FFAA01"),
                                                                        scale=fl.Scale(scale_x=-1, scale_y=1)
                                                                    ),
                                                                    Column(
                                                                        controls=[
                                                                            Text("Seguir a coleta seletiva",
                                                                                 size=15,
                                                                                 weight=FontWeight.BOLD
                                                                                 ),
                                                                            Text(
                                                                                "Verifique os pontos de coleta seletiva do município.",
                                                                                width=265
                                                                            )
                                                                        ],
                                                                        spacing=2,
                                                                        margin=Margin.only(top=15)

                                                                    )
                                                                ]
                                                            ),

                                                        ],
                                                        margin=Margin.only(left=30),
                                                        spacing=2
                                                    )
                                                ),
                                            ],
                                            spacing=1
                                        ),
                                    ),

                                    Container(
                                        content=Column(
                                            controls=[
                                                Row(
                                                    controls=[
                                                        Text(f"Encontre Ecopontos Proximos:",
                                                             size=18,
                                                             weight=FontWeight.BOLD,
                                                             color="#797D7C",
                                                             italic=True
                                                             ),
                                                    ],
                                                    margin=Margin.only(left=15),
                                                ),
                                                Container(
                                                    content=Column(
                                                        controls=[

                                                            FilledButton(
                                                                "Veja Áreas de Reciclagem em sua Cidade...",
                                                                Container(
                                                                    width=25,
                                                                    height=25,
                                                                    alignment=Alignment.CENTER,
                                                                    content=Icon(Icons.LOCATION_ON, color="#FFAA01"),
                                                                    scale=fl.Scale(scale_x=-1, scale_y=1)
                                                                ),
                                                                on_click=lambda: abrir_web(
                                                                    "https://www.rotadareciclagem.com.br/"),
                                                                icon_color="#595C5B",
                                                                width=300,
                                                                height=60,
                                                                bgcolor="#FFD980",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=15))

                                                            ),
                                                        ],
                                                        margin=Margin.only(left=30),
                                                        spacing=8
                                                    )
                                                ),
                                            ],
                                            spacing=10
                                        ),
                                    ),
                                    Container(
                                        content=Column(
                                            controls=[
                                                Row(
                                                    controls=[
                                                        Text(f"Sites:",
                                                             size=18,
                                                             weight=FontWeight.BOLD,
                                                             color="#797D7C",
                                                             italic=True
                                                             ),
                                                    ],
                                                    margin=Margin.only(left=15),
                                                ),
                                                Container(
                                                    content=Row(
                                                        controls=[

                                                            FilledButton(
                                                                Text("Ver mais sobre",
                                                                     size=11, weight=FontWeight.BOLD),

                                                                on_click=lambda: abrir_web(
                                                                    "https://ambiental.sc/blog/como-e-feita-a-reciclagem-de-papel/"),
                                                                icon_color="#595C5B",
                                                                width=100,
                                                                height=60,
                                                                bgcolor="#FFD980",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=20))

                                                            ),
                                                            FilledButton(
                                                                Text("Ideias reciclagem",
                                                                     size=11, weight=FontWeight.BOLD),

                                                                on_click=lambda: abrir_web(
                                                                    "https://br.pinterest.com/viladoartesao/artesanato-com-papel/"),
                                                                icon_color="#595C5B",
                                                                width=105,
                                                                height=60,
                                                                bgcolor="#FFD980",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=20))

                                                            ),

                                                            FilledButton(
                                                                Text("Canal Youtube",
                                                                     size=11, weight=FontWeight.BOLD),

                                                                on_click=lambda: abrir_web(
                                                                    "https://www.youtube.com/playlist?list=PLg54jVJRnbpi8G5DbizNnlptahTlEKXwy"),
                                                                icon_color="#595C5B",
                                                                width=100,
                                                                height=60,
                                                                bgcolor="#FFD980",
                                                                color=Colors.GREY_800,
                                                                style=fl.ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=20))

                                                            ),
                                                        ],

                                                        margin=Margin.only(left=30),
                                                        spacing=8
                                                    ),

                                                ),
                                            ],
                                            spacing=10
                                        ),
                                    )
                                ],
                                spacing=15,
                                scroll=fl.ScrollMode.ALWAYS,
                            ),

                        ),

                    ],
                    spacing=5,
                ),

            )

    # Voltar

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route("/pagina_inicial")

    # Componentes

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


fl.run(main)
