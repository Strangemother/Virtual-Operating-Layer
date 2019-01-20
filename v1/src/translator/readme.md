# Translator

VOL CORE or any inputting unit of work will display text and graphics

A unit to convert content from visual streams into the container and its visual ability.

The translator is split into two parts - the receiver and rendering unit. The information is piped to a container for rendering.

## Base

The root unit to extend.


## Outputs

The translator will handle the conversion of graphic API calls to the correct output.
A call to the API may be simple or complex. Simple calls contain basic routines to execute -
such as Text to a default text presenter, or session data streaming.

Target outputs for a VOL:

    framebuffer
        The standard linux print framebuffer - directly from translation of data output

    XDisplay
        An xdisplay would be nice, displaying the _container_ content and using the same
        tooling - however this is a lower priority.

    container
        A purpose build visual container to render VOL on a HOST machine -
        it comes complete with a layered API for

        Vector
        Pixel
        GL

## Interfaces

The output device is chosen through the interface bur 'drivers' for different platforms reside within
the translator. standard put is the display device such as the onboard default out.

The "container" is a unique output purpose built for the entire VOL to redirect all information to one relative session
without higher-level understanding. It also contains a range of display methods. Natively it can live within any XDisplay,
therefore presentation is distinct from the VOL and can operate remotely.

Other interfaces includes off-the-shelf GPIO and UART. For leveraging Node and Shard strategies.
As the _standard_ routines exist, implementing sub translators for non-standard (but common) displays will help leverage the VOL's
distribution and small footprint.

+ OTS OLED displays, catering 0.9inch to8inch
+ GPIO / UART Framed buffering
+ SOC Displays such as OTS API touch screens

