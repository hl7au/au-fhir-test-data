<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:fhir="http://hl7.org/fhir"
	xmlns:html="http://www.w3.org/1999/xhtml">

	<xsl:template match="/fhir:Bundle">
		<xsl:text>mkdir quarantined&#xA;</xsl:text>
		<xsl:apply-templates/>
	</xsl:template>

	<xsl:template
		match="/fhir:Bundle/fhir:entry/fhir:resource/fhir:OperationOutcome[fhir:text/html:div/html:table/html:tr/html:td='error']/fhir:extension[@url = 'http://hl7.org/fhir/StructureDefinition/operationoutcome-file']/fhir:valueString">
		<xsl:text>mv </xsl:text>
		<xsl:value-of select="./@value" />
		<xsl:text> quarantined</xsl:text>
		<xsl:text>&#xA;</xsl:text>
	</xsl:template>

	<xsl:template match="text()" />

	<xsl:output method="text" encoding="utf-8"
		media-type="string" />
</xsl:stylesheet>