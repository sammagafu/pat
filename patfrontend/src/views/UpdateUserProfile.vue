<template>
    <section class="py-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <AuthSideBar />
                </div>
                <div class="col-md-8">
                    <div class="mb-4">
                        <h2>Update {{ user.first_name }}'s Profile</h2>
                    </div>
                    <form class="inner-add-comments form-contact-1" id="registration-form" @submit.prevent="updateUser">
                <div class="row">
                    <div class="col-md-6">

                        <div class="mb-3">
                            <div class="form-group">
                                <label for="firstname">First Name <span style="color: red">*</span></label>
                                <input type="text" v-model="firstname" class="form-control" id="firstname" required>

                            </div>
                        </div>
                        <div class="mb-3">
                            <div class="form-group">
                                <label for="middlename">Middle name <span style="color: red">*</span></label>
                                <input type="text" v-model="middlename" class="form-control" id="middlename" required>

                            </div>
                        </div>
                        <div class="mb-3">
                            <div class="form-group">
                                <label for="lastname">Last Name <span style="color: red">*</span></label>
                                <input type="text" v-model="lastname" class="form-control" id="lastname" required>

                            </div>
                        </div>
                        <div class="mb-3">
                            <div class="form-group">
                                <label for="phonenumber">Phone Number (Start with +255)</label>
                                <input type="phone" v-model="phone" class="form-control" id="phonenumber" required>
                            </div>
                        </div>

                        <div class="mb-3">
                            <label for="gender">Gender <span style="color: red">*</span></label>
                            <select name="gender" class="form-control" v-model="gender" id="gender">
                                <option value="Male">Male</option>
                                <option value="Female">Female</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label for="region">Region <span style="color: red">*</span></label>
                            <select class="form-control" v-model="region" id="region">
                                <option value="Arusha">Arusha</option>
                                <option value="Dar es Salaam">Dar es Salaam</option>
                                <option value="Dodoma">Dodoma</option>
                                <option value="Geita">Geita</option>
                                <option value="Iringa">Iringa</option>
                                <option value="Kagera">Kagera</option>
                                <option value="Katavi">Katavi</option>
                                <option value="Kigoma">Kigoma</option>
                                <option value="Kilimanjaro">Kilimanjaro</option>
                                <option value="Lindi">Lindi</option>
                                <option value="Manyara">Manyara</option>
                                <option value="Mara">Mara</option>
                                <option value="Mbeya">Mbeya</option>
                                <option value="Mjini Magharibi">Mjini Magharibi</option>
                                <option value="Morogoro">Morogoro</option>
                                <option value="Mtwara">Mtwara</option>
                                <option value="Mwanza">Mwanza</option>
                                <option value="Njombe">Njombe</option>
                                <option value="Pemba North">Pemba North</option>
                                <option value="Pemba South">Pemba South</option>
                                <option value="Pwani">Pwani</option>
                                <option value="Rukwa">Rukwa</option>
                                <option value="Ruvuma">Ruvuma</option>
                                <option value="Shinyanga">Shinyanga</option>
                                <option value="Simiyu">Simiyu</option>
                                <option value="Singida">Singida</option>
                                <option value="Songwe">Songwe</option>
                                <option value="Tabora">Tabora</option>
                                <option value="Tanga">Tanga</option>
                                <option value="Unguja North">Unguja North</option>
                                <option value="Unguja South">Unguja South</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label>Please select the profession that most closely represents you <span
                                    style="color: red">*</span></label>
                            <select class="form-control" name="profession" v-model="profession">
                                <option value="Administrator">Administrator</option>
                                <option value="Community health worker">ommunity health worker</option>
                                <option value="First responder such as EMT or Paramedic">First responder such as EMT or
                                    Paramedic</option>
                                <option value="Mental health provider such as counselor, psychologist, social worker">
                                    Mental
                                    health provider such as counselor, psychologist, social worker</option>
                                <option value="Nurse or practitioner or physician assistant">Nurse or practitioner or
                                    physician
                                    assistant</option>
                                <option value="Pharmacist">Pharmacist</option>
                                <option value="Paediatrician">Paediatrician</option>
                                <option value="Public health official">Public health official</option>
                                <option value="Testing or laboratory personnel">Testing or laboratory personnel</option>
                                <option value="Teacher/educator">Teacher/educator</option>
                                <option value="Researcher">Researcher</option>
                                <option value="Student">Student</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label>Your organization Name<span style="color: red">*</span></label>
                            <input type="text" v-model="organization" class="form-control"
                                placeholder="Bugando Medical Center" required>
                        </div>

                        <div class="mb-3">
                            <label>Area of work or Industry <span style="color: red">*</span></label>
                            <select class="form-control" v-model="industry">
                                <option value="Work">Work</option>
                                <option value="Hospital">Hospital</option>
                                <option value="Community healthcare">Community healthcare</option>
                                <option value="Nursing/care facility">Nursing/care facility</option>
                                <option value="Public health">Public health</option>
                                <option value="Non-governmental organization">Non-governmental organization
                                </option>
                                <option value="School/university">School/university</option>
                                <option value="Government">Government</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <div class="form-group">
                                <label class="control-label ">Membership type</label>
                                <select class="form-control" v-model="typeofmember">
                                    <option value="Associate Member">Associate Member</option>
                                    <option value="Ordinary Member">Ordinary Member</option>
                                </select>
                            </div>
                        </div>

                        <div class="mb-3">
                            <div class="form-group">
                                <label class="control-label" for="avatar">Avatar (Add your passport for your ID or you can update later)</label>
                                <br>
                                <input type="file" name="image" id="avatar" placeholder="passport image for your avatar" @change="onFileUpload" ref="avatar">
                            </div>
                        </div>

                        <!-- <template v-if="typeofmember == Ordinary Member">
                        </template> -->
                        <span v-if="typeofmember == 'Ordinary Member'">
                            <div class="mb-3">
                                <div class="form-group">
                                    <label for="mct">MCT number (optional)</label>
                                    <input type="text" v-model="mct" class="form-control" id="mct" placeholder="192000">
                                </div>
                            </div>

                            <div class="mb-3">
                                <div class="form-group">
                                    <label for="masters">Enter the year that you graduated for masters</label>
                                    <input type="text" v-model="year" class="form-control" id="year" placeholder="2007">
                                </div>
                            </div>

                            <div class="mb-3">
                                <div class="form-group">
                                    <label for="graduated">Enter the Institute attended</label>
                                    <input type="text" v-model="masters" class="form-control" id="graduated" placeholder="Muhimbili university of health and allied Sciences">
                                </div>
                            </div>

                        </span>

                        <button class="btn btn-primary btn-user mt-4 btn-block">
                            Update To PAT
                        </button>

                    </div>
                </div>
            </form>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import AuthSideBar from '../components/AuthSideBar.vue';
import { authStore } from '../stores/usersStore';
import axios from 'axios';
import { ref, onMounted } from 'vue'
export default {
    components : {
        AuthSideBar 
    },
    setup() {
        // const 
        const authdata = authStore()
        const user = ref({})
        const firstname = ref('')
        const middlename = ref('')
        const lastname = ref('')
        const phone = ref('')
        const mct = ref('')
        const gender = ref('')
        const region = ref('')
        const profession = ref('')
        const organization = ref('')
        const industry = ref('')
        const typeofmember = ref('')
        const graduation = ref('')
        const masters = ref('')
        const year = ref('')
        const msg = ref([])

        const token = authdata.token
        
        // function onUnmounted(callback: () => void): void
        onMounted(() => {
            axios.get('auth/users/me/',{
                headers: {
                    "Authorization" : `Bearer ${token}`
                }
            })
                .then(response => {
                    firstname.value = response.data.first_name
                    middlename.value = response.data.middle_name
                    lastname.value = response.data.last_name
                    phone.value = response.data.phone
                    mct.value = response.data.mctnumber
                    typeofmember.value = response.data.typeofmember
                    region.value = response.data.region
                    gender.value = response.data.gender
                    profession.value = response.data.profession
                    organization.value = response.data.organization
                    industry.value = response.data.areaofwork
                    graduation.value = response.data.graduation
                    masters.value = response.data.masters
                    year.value = response.data.year
                })
                .catch(error => {
                    console.log(error);
                });

        })

        function updateUser(){
            const data = {
                'first_name' : firstname.value,
                'middle_name' : middlename.value,
                'last_name': lastname.value,
                'phone': phonenumber.value,
                'mctnumber': mct.value,
                'gender': gender.value,
                'region': region.value,
                'profession': profession.value,
                'organization': organization.value,
                'areaofwork': industry.value,
                'typeofmember': typeofmember.value,
                'collage':masters.value,
                'year':year.value,
            }
            axios.put('auth/users/me/',data,{
                headers: {
                    "Authorization" : `Bearer ${token}`
                }
            })
                .then(response => {
                    // console.log(response.data)
                    firstname.value = response.data.first_name

                })
                .catch(error => {
                    console.log(error);
                });
        }


        return {
            firstname,middlename,lastname,phone,mct,gender,region,profession,organization,industry,typeofmember,graduation,masters,year,
            user,authdata,updateUser
        }
    }
}
</script>

<style scoped>
.avatar{
    margin-bottom: 18px;
}
img{
    width: 200px !important;
}
</style>