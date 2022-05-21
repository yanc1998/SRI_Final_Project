<template>
  <div class="container">
    <b-form>
      <b-form-input v-model="query" placeholder="Enter the file content"></b-form-input>
      <b-col lg="4" class="pb-2">
        <b-button @click="find" variant="primary">Find</b-button>
      </b-col>
    </b-form>
    <div>
      <b-list-group>
        <b-list-group-item button v-for="item in this.relevantDocuments">{{
            item
          }}
        </b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "find",
  data() {
    return {
      query: '',
      relevantDocuments: []
    }
  },
  methods: {
    find() {

      const data = JSON.stringify({
        "query": "testz",
        "count": 5
      });

      const config = {
        method: 'post',
        url: 'http://127.0.0.1:5000/find',
        headers: {
          'Content-Type': 'application/json'
        },
        data: data
      };

      axios(config)
          .then((response) => {
            console.log(JSON.stringify(response.data["data"]));
            this.relevantDocuments = response.data["data"]
          })
          .catch(function (error) {
            console.log(error);
          });

    }

  }
}
</script>

<style scoped>

</style>
