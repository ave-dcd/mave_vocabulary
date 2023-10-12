JSYAMLS:=experiment.yml
JSONS:=${JSYAMLS:.yml=.json}

all: ${JSONS}

%.json: %.yml
	jsy2js.py <$< >$@
