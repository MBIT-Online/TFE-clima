El cambio climático global es una realidad que afectará a la humanidad en todo el mundo. Este tendrá diferentes efectos en cada localización y época del año y seremos sacudidos tanto por inundaciones como por olas de calor.

Según nuestra hipótesis, las personas tienen dificultades para obtener esta información y las consecuencias que pueden tener en su vida diaria o sus sectores de trabajo.

Para ello nosotros presentamos el proyecto “Clima for World” (Clim4World), donde ayudaremos a los usuarios a visualizar cuáles son los riesgos climáticos en su localización, para que puedan tomar decisiones al respecto, como compra de una casa, elección del lugar de vacaciones o tipo de cultivo

Para llevar a cabo este proyecto, hemos analizado numerosas fuentes de datos meteorológicos, históricos, actuales y proyectados, para realizar nuestros propios análisis y sacar nuestras propias conclusiones. Para ello hemos creado una serie de herramientas de extracción, procesamiento, modelado y visualización de datos utilizando la infraestructura de AWS.

Nuestros modelos han corroborado la realidad del cambio climático y nos muestran que las temperaturas han aumentado en los últimos 70 años y seguirán haciéndolo en los próximos años. Aunque estos cambios han sido distintos en las diferentes localizaciones.

Para facilitar la visualización de estos resultados hemos construido una aplicación llamada “Clim4World”, que consta de tres secciones donde se pueden consultar los diferentes riesgos
  - “Historicista”: Temperaturas y lluvias pasadas y sus riesgos para la salud.
  - “Futurista”:
      - Proyección de temperaturas en el futuro, calculadas por nosotros a partir de los datos históricos.
      - Zonas con altas probabilidades de inundación en toda España.
  - “Actualista”: Predicciones a 15 días de temperaturas y precipitaciones en varias localidades de la Comunidad Valenciana.

En cada una de las diferentes carpetas hemos desarrollado una parte diferente del proyecto:
  - Extracción de datos:
      - las libretas con las cuales extraemos la información pública de la AEMET.
      - las libretas con las cuales extraemos las predicciones de WeatherBit.
  - Procesamiento y Modelado de datos CORDEX:
      - la libreta donde extraemos los datos públicos de ESGF.
      - la libreta donde procesamos y modelamos los datos para obtener un índice de aridez.
  - Procesamiento y Modelado de datos AEMET:
      - las libretas de procesamiento de los datos de la AEMET de la Comunidad Valenciana.
      - los datasets resultantes
      - los modelos entrenados
  
  - Proyecto streamlit:
      - la aplicación “Clim4World” al completo que hemos realizado alrededor de la información extraída, procesada y modelada.

Muchas gracias.
    


