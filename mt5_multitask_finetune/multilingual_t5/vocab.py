# Copyright 2022 The mT5 Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Defines the vocabulary for multilingual t5."""

import t5

DEFAULT_SPM_PATH = "/raid/yiptmp/huggingface-models/mt5_vocab/sentencepiece.model"

DEFAULT_EXTRA_IDS = 100
DEFAULT_VOCAB = t5.data.SentencePieceVocabulary(DEFAULT_SPM_PATH)
