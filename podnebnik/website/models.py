import itertools

from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock

import podnebnik.visualisations


ALIGNMENT_CHOICES = [
    ("left", "Left"),
    ("right", "Right"),
    ("center", "Center"),
]


# -----------------------------------------------------------------------------
# Blocks
class ImageBlock(blocks.StructBlock):

    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)
    alignment = blocks.ChoiceBlock(choices=ALIGNMENT_CHOICES, required=False)

    class Meta:
        icon = "image"
        template = "website/blocks/image.html"


class VisualisationBlock(blocks.StructBlock):

    def get_visualization_choices():
        return [(id, name) for (id, name, _) in podnebnik.visualisations.VISUALISATIONS]

    visualisation = blocks.ChoiceBlock(choices=get_visualization_choices)
    caption = blocks.RichTextBlock(required=False, features=['bold', 'italic', 'link', 'document-link'])

    class Meta:
        icon = "image"


class MixedContentBlock(blocks.StreamBlock):

    text = blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'blockquote', 'hr', 'link', 'document-link', 'image'])
    visualisation = VisualisationBlock()
    image = ImageBlock()
    video = EmbedBlock()
    table = TableBlock()
    references = blocks.RichTextBlock()
    raw_html = blocks.RawHTMLBlock(help_text="Use only when all else fails")

    class Meta:
        template = "website/blocks/mixed-content.html"


# -----------------------------------------------------------------------------
# Pages

class HomePage(Page):

    lead = RichTextField()

    template = "website/pages/home.html"

    content_panels = Page.content_panels + [
        FieldPanel("lead"),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        # context["articles"] = ArticlePage.objects.live()
        context["articles"] = [
            ("CO₂ and Greenhouse Gas Emissions", ["Greenhouse Gas Emissions"], "17. marec 2021"),
            ("Outdoor Air Pollution", ["Greenhouse Gas Emissions", "Pollution"], "17. marec 2021"),
            ("Age Structure", ["Population"], "17. marec 2021"),
            ("Access to Energy", ["Energy"], "17. marec 2021"),
            ("Ozone Layer", ["Greenhouse Gas Emissions"], "17. marec 2021"),
            ("Water Use and Stress", ["Environment", "Water"], "17. marec 2021"),
            ("Environmental impacts of food production", ["Environment"], "17. marec 2021"),
            ("Forests and Deforestation", ["Environment"], "17. marec 2021"),
            ("Indoor Air Pollution", ["Greenhouse Gas Emissions", "Pollution"], "17. marec 2021"),
            ("Renewable Energy", ["Energy"], "17. marec 2021"),
            ("Fossil Fuels", ["Energy"], "17. marec 2021"),
            ("Air Pollution", ["Greenhouse Gas Emissions", "Pollution"], "17. marec 2021"),
            ("Plastic Pollution", ["Energy", "Pollution"], "17. marec 2021"),
            ("World Population Growth", ["Population"], "17. marec 2021"),
        ]

        return context


class ArticlePage(Page):

    lead = RichTextField(null=True, blank=True)

    body = StreamField(MixedContentBlock(null=True, blank=True))

    main_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    blurb = RichTextField()

    template = "website/pages/article.html"

    content_panels = Page.content_panels + [
        FieldPanel("lead"),
        StreamFieldPanel("body"),
        MultiFieldPanel([
            FieldPanel("blurb"),
            ImageChooserPanel("main_image"),
        ], heading="Promote on homepages"),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context["visualisations"] = [
            {'id': '{}-visualisation-{}'.format(el.value["visualisation"], i), 'template': 'visualisations/{}.html'.format(el.value["visualisation"])}
            for (i, el)
            in enumerate(self.body) if el.block_type == "visualisation"
        ]

        visualisations_data_functions_dict = {id: data_function for (id, _, data_function) in podnebnik.visualisations.VISUALISATIONS if data_function is not None}
        visualisations_data_functions = set(itertools.chain.from_iterable([
            visualisations_data_functions_dict.get(visualisation, [])
            for visualisation
            in set([el.value["visualisation"] for el in self.body if el.block_type == "visualisation"])
        ]))

        context["visualisations_data"] = [f() for f in visualisations_data_functions]

        return context


class GeneralPage(Page):

    body = StreamField(MixedContentBlock())

    template = "website/pages/general.html"

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]
