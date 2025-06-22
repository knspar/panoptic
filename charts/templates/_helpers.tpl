{{- define "justniffer-stack.name" -}}
{{- .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.fullname" -}}
{{- $name := .Chart.Name }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}

{{- define "justniffer-stack.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.labels" -}}
helm.sh/chart: {{ include "justniffer-stack.chart" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{- define "justniffer-stack.daemon.selectorLabels" -}}
app.kubernetes.io/name: {{ include "justniffer-stack.daemon.name" . }}
app.kubernetes.io/component: daemon
{{- end }}

{{- define "justniffer-stack.operator.selectorLabels" -}}
app.kubernetes.io/name: {{ include "justniffer-stack.operator.name" . }}
app.kubernetes.io/component: operator
{{- end }}

{{- define "justniffer-stack.proxy.selectorLabels" -}}
app.kubernetes.io/name: {{ include "justniffer-stack.proxy.name" . }}
app.kubernetes.io/component: proxy
{{- end }}

{{- define "justniffer-stack.daemon.name" -}}
{{- (printf "%s-daemon" (include "justniffer-stack.fullname" .))  | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.operator.name" -}}
{{- (printf "%s-operator" (include "justniffer-stack.fullname" .)) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.proxy.name" -}}
{{- (printf "%s-proxy" (include "justniffer-stack.fullname" .)) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.proxy.service.name" -}}
{{- (printf "%s-proxy-service" (include "justniffer-stack.fullname" .)) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.proxy.serviceAccountName" -}}
{{- (printf "%s-proxy" (include "justniffer-stack.fullname" .)) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.daemon.serviceAccountName" -}}
{{- (printf "%s-daemon" (include "justniffer-stack.fullname" .)) | trunc 63 | trimSuffix "-" }}
{{- end }}


{{- define "justniffer-stack.operator.serviceAccountName" -}}
{{- (printf "%s-operator" (include "justniffer-stack.fullname" .)) | trunc 63 | trimSuffix "-" }}
{{- end }}


{{- define "justniffer-stack.apiSecretName" -}}
{{- printf "%s-apikey" (include "justniffer-stack.fullname" .) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.roleName" -}}
{{- (printf "%s-pods-reader" (include "justniffer-stack.fullname" .))  | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.roleBindingName" -}}
{{- (printf "%s-pods-reader-binding" (include "justniffer-stack.fullname" .)) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.operator.roleName" -}}
{{-  (printf "%s-operator-role" (include "justniffer-stack.fullname" .))  | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.operator.roleBindingName" -}}
{{-  (printf "%s-operator-role-binding" (include "justniffer-stack.fullname" .)) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "justniffer-stack.configPathDir" -}}
{{- (printf "/mnt/etc/justniffer") -}}
{{- end -}}

{{- define "justniffer-stack.configPathFile" -}}
{{- (printf "%s/extractors" (include "justniffer-stack.configPathDir" .)) -}}
{{- end -}}


{{- define "justserver-image" -}}
{{- (printf "knspar/phronetis:0.1.46") -}}
{{- end -}}

{{- define "justernetes-image" -}}
{{- (printf "knspar/phronetis-operator:0.1.6") -}}
{{- end -}}


{{- define "justniffer-stack.standardProbe" -}}
{{ .probeType }}:
  httpGet:
    path: /health  
    port: http
  initialDelaySeconds: 5  
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 3
{{- end }}