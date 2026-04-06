# Sistema de Reposición de Logística
>Nota: Los datos presentados corresponden a una empresa del sector comercial de repuestos automotrices. La información ha sido anonimizada con el fin de proteger datos sensibles y garantizar la confidencialidad de la organización.
<p>
Proyecto de análisis de reposición de inventario mediante el procesamiento de datos en Python y visualización en Power BI.
</p>

[![Python](https://img.shields.io/badge/Python-3.12.10-blue?logo=python)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-Report-yellow?logo=microsoft-power-bi)](https://powerbi.microsoft.com/)
![Status](https://img.shields.io/badge/Status-Concluido-green)
</p>

## Objetivos:


<ul>
	<li>Desarrollar un sistema basado en datos.</li>
	<li>Identificar productos críticos en relación con su comportamiento histórico.</li>
	<li>Analizar la demanda y mejorar la toma de decisiones.</li>
	<li>Reducir el tiempo de procesamiento y actualización de los datos.</li>
</ul>
</p>

## Proceso:

<ol>
<li>Extracción y Limpieza de Datos:</li>
	<ul>
	<li>Extracción de información de la fuente de datos.</li>
	<li>Tratamiento de valores nulos y espacios limites innecesarios.</li>
	<li>Estandarización de formatos.</li>
	<li>Exportación de tablas.</li>
	</ul>
<li>Procesamiento y Análisis:</li>
	<ul>
		<li>Administración de relaciones entre tablas.</li>
		<li>Cálculo de totales (Venta Neto, Venta Promedio, Venta Maxima).</li>
		<li>Ventas acumuladas.</li>
		<li>Porcentaje acumulado.</li>
	</ul>
<li>Clasificación ABC y Evaluación de Reposición:</li>
	<ul>
		<li>Identificación de productos críticos.</li>
		<li>Segmentación por importancia.</li>
		<li>Evaluación de resultados y asignación de estado de reposición.</li>
		<li>Segmentación por categoría y año.</li>
	</ul>
<li>Visualización:</li>
	<ul>
		<li>Dashboard en Power BI.</li>
		<li>KPIs de rendimiento y comparación entre periodos.</li>
		<li>Análisis de comportamiento mensual.</li>
	</ul>
</ol>
</p>

## Resultados:

<ul>
	<li>Evaluación de comportamiento de productos por mes.</li>
	<li>Detección de picos de demanda.</li>
	<li>Reducción del tiempo de procesamiento y actualización de datos de 1 minutos a 30 segundos por actualización de información en la fuente de datos.</li>
	<li>Clasificación ABC  por priorización de inventario.</li>
</ul>
</p>

## Estructura del Proyecto:

La estructura del proyecto realizado es el siguiente:
<p>PT_Reposicion_Logistica</p>
<ol>
	<li>data/</li>
		<ol>
			<li>raw/</li>
			<li>clean/</li>
			<li>templates/</li>
		</ol>
	<li>scripts/</li>
	<li>readme/</li>
</ol>
</p>

## Información Importante:

>Nota sobre el archivo Power BI: El archivo utiliza una ruta **parametrizada**, por si los datos no cargan correctamente:

<ol>
<li>Ir a Transformar datos.</li>
<li>Editar el parámetro Ruta Base.</li>
<li>Ajustar la ruta a la ubicación local.</li>
</ol>
</p>

## Autor:

<p>
Proyecto desarrollado por Aldair Leandro como parte de su formación en análisis de datos y mejora de procesos logísticos.
</p>
